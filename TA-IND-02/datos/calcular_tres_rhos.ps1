# Equivalente en PowerShell 5 de calcular_tres_rhos.py.
# Se uso porque Python 3 no estaba instalado en el equipo de trabajo.
# Solo usa la biblioteca estandar; escribe tres_rhos.csv en UTF-8 sin BOM.

$base = $PSScriptRoot
$utf8 = New-Object Text.UTF8Encoding($false)

$m = Import-Csv (Join-Path $base 'moscow.csv') -Encoding UTF8
$v = Import-Csv (Join-Path $base 'votacion.csv') -Encoding UTF8
$c = Import-Csv (Join-Path $base 'kano_caracteristicas.csv') -Encoding UTF8
$r = Import-Csv (Join-Path $base 'kano_respuestas.csv') -Encoding UTF8

$valor = @{ 'M' = 4; 'S' = 3; 'C' = 2; 'W' = 1 }
$mos = @{}
foreach ($f in $m) { $mos[$f.requisito] = [double]$valor[$f.moscow] }

$tot = @{}
$sumas = @{}
foreach ($f in $v) {
  if (-not $tot.ContainsKey($f.requisito)) { $tot[$f.requisito] = 0.0 }
  $tot[$f.requisito] += [double]$f.puntos
  if (-not $sumas.ContainsKey($f.participante)) { $sumas[$f.participante] = 0.0 }
  $sumas[$f.participante] += [double]$f.puntos
}
if (@($sumas.Values | Where-Object { $_ -ne 100 }).Count -gt 0) {
  throw "Cada votante debe sumar 100; se obtuvo: $(($sumas.GetEnumerator() | ForEach-Object { "$($_.Key)=$($_.Value)" }) -join ', ')"
}

function Get-Ranks {
  param([object[]]$pairs)
  $orden = @($pairs | Sort-Object -Property value)
  $res = @{}
  $i = 0
  while ($i -lt $orden.Count) {
    $j = $i
    while (($j + 1 -lt $orden.Count) -and ($orden[$j + 1].value -eq $orden[$i].value)) { $j++ }
    $rango = (($i + 1) + ($j + 1)) / 2.0
    for ($k = $i; $k -le $j; $k++) { $res[$orden[$k].key] = $rango }
    $i = $j + 1
  }
  return $res
}

function Get-Rho {
  param([double[]]$x, [double[]]$y)
  $mx = ($x | Measure-Object -Average).Average
  $my = ($y | Measure-Object -Average).Average
  $num = 0.0; $dx = 0.0; $dy = 0.0
  for ($i = 0; $i -lt $x.Count; $i++) {
    $a = $x[$i] - $mx
    $b = $y[$i] - $my
    $num += $a * $b
    $dx += $a * $a
    $dy += $b * $b
  }
  return ($num / [math]::Sqrt($dx * $dy))
}

$idx = @{}
$idx['me gusta'] = 0
$idx['espero que sea as' + [char]0x00ED] = 1
$idx['me resulta indiferente'] = 2
$idx['puedo aceptarlo'] = 3
$idx['no me gusta'] = 4

$tab = @(
  @('Q','A','A','A','O'),
  @('R','I','I','I','M'),
  @('R','I','I','I','M'),
  @('R','I','I','I','M'),
  @('R','R','R','R','Q')
)

$con = @{}
foreach ($f in $r) {
  $ch = $f.caracteristica
  if (-not $con.ContainsKey($ch)) {
    $con[$ch] = @{ 'A'=0.0; 'I'=0.0; 'M'=0.0; 'O'=0.0; 'R'=0.0; 'Q'=0.0 }
  }
  $cat = $tab[[int]$idx[$f.respuesta_funcional]][[int]$idx[$f.respuesta_disfuncional]]
  $con[$ch][$cat] += 1.0
}

$better = @{}
foreach ($f in $c) {
  $n = $con[$f.id]
  $better[$f.requisito_relacionado] = ($n['A'] + $n['O']) / 5.0
}

$ids20 = @($mos.Keys | Sort-Object)
$rm20 = Get-Ranks @($ids20 | ForEach-Object { [pscustomobject]@{ key=$_; value=$mos[$_] } })
$rv20 = Get-Ranks @($ids20 | ForEach-Object { [pscustomobject]@{ key=$_; value=$tot[$_] } })
$xm20 = [double[]]@($ids20 | ForEach-Object { $rm20[$_] })
$xv20 = [double[]]@($ids20 | ForEach-Object { $rv20[$_] })
$rho20 = Get-Rho $xm20 $xv20

$comunes = @($better.Keys | Sort-Object)
$rm = Get-Ranks @($comunes | ForEach-Object { [pscustomobject]@{ key=$_; value=$mos[$_] } })
$rv = Get-Ranks @($comunes | ForEach-Object { [pscustomobject]@{ key=$_; value=$tot[$_] } })
$rk = Get-Ranks @($comunes | ForEach-Object { [pscustomobject]@{ key=$_; value=$better[$_] } })
$xm = [double[]]@($comunes | ForEach-Object { $rm[$_] })
$xv = [double[]]@($comunes | ForEach-Object { $rv[$_] })
$xk = [double[]]@($comunes | ForEach-Object { $rk[$_] })

$filas = @(
  [pscustomobject]@{ comparacion='MoSCoW-voto (20 requisitos)'; n=$ids20.Count; rho=('{0:F4}' -f $rho20) },
  [pscustomobject]@{ comparacion='MoSCoW-Kano (8 enlazados)'; n=$comunes.Count; rho=('{0:F4}' -f (Get-Rho $xm $xk)) },
  [pscustomobject]@{ comparacion='MoSCoW-voto (8 enlazados)'; n=$comunes.Count; rho=('{0:F4}' -f (Get-Rho $xm $xv)) },
  [pscustomobject]@{ comparacion='Kano-voto (8 enlazados)'; n=$comunes.Count; rho=('{0:F4}' -f (Get-Rho $xk $xv)) }
)

$salida = Join-Path $base 'tres_rhos.csv'
$sb = New-Object Text.StringBuilder
[void]$sb.AppendLine('comparacion,n,rho')
foreach ($f in $filas) { [void]$sb.AppendLine("$($f.comparacion),$($f.n),$($f.rho)") }
[IO.File]::WriteAllText($salida, $sb.ToString(), $utf8)
$filas | Format-Table -AutoSize
