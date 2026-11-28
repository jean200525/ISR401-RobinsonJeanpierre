$repo = 'C:\Users\Jean Pierre Robinson\AppData\Local\Temp\opencode\jean-ind02-repo'
$csv = Join-Path $repo 'TA-IND-02\datos\moscow.csv'
$out = Join-Path $repo 'TA-IND-02\secciones\tabla_requisitos.tex'
$utf8 = New-Object Text.UTF8Encoding($false)

function Esc($s) {
  return ([string]$s).Replace('%', '\%').Replace('_', '\_').Replace('&', '\&').Replace('#', '\#').Replace('$', '\$')
}

$filas = Import-Csv $csv -Encoding UTF8
$cabecera = @(
  '\footnotesize',
  '\begin{longtable}{@{}p{0.9cm}@{\hspace{0.15cm}}p{0.7cm}@{\hspace{0.15cm}}p{4.2cm}@{\hspace{0.15cm}}p{0.6cm}@{\hspace{0.15cm}}p{0.6cm}@{\hspace{0.15cm}}p{3.7cm}@{\hspace{0.15cm}}p{4.0cm}@{}}',
  '\caption{Lista final de los 20 requisitos con ID, tipo, clase MoSCoW, horas, justificación y criterio verificable.}\\',
  '\toprule',
  'ID & Tipo & Enunciado & M & h & Justificacion & Criterio \\',
  '\midrule',
  '\endhead',
  '\bottomrule',
  '\endlastfoot'
)
$cuerpo = @()
foreach ($f in $filas) {
  $tipo = if ($f.tipo -like 'Calidad*') { 'Q' } else { 'F' }
  $cuerpo += '{0} & {1} & {2} & {3} & {4} & {5} & {6} \\' -f `
    (Esc $f.requisito), $tipo, (Esc $f.enunciado), `
    (Esc $f.moscow), (Esc $f.horas), (Esc $f.justificacion), (Esc $f.criterio_verificacion)
}
$lineas = $cabecera + $cuerpo + @('\end{longtable}', '\label{tab:requisitos}')
[IO.File]::WriteAllText($out, (($lineas -join "`n") + "`n"), $utf8)
"escrito: $out ($($cuerpo.Count) filas)"
