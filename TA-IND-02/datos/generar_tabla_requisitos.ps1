$repo = 'C:\Users\Jean Pierre Robinson\AppData\Local\Temp\opencode\jean-ind02-repo'
$csv = Join-Path $repo 'TA-IND-02\datos\moscow.csv'
$out = Join-Path $repo 'TA-IND-02\secciones\tabla_requisitos.tex'
$utf8 = New-Object Text.UTF8Encoding($false)

function Esc($s) {
  return ([string]$s).Replace('%', '\%').Replace('_', '\_').Replace('&', '\&').Replace('#', '\#').Replace('$', '\$')
}

$filas = Import-Csv $csv -Encoding UTF8
$lineas = @(
  '\textbf{Requisitos formulados: 20 en total, 12 funcionales y 8 de calidad. F = funcional, Q = calidad; M = Must, S = Should, C = Could, W = Won''t.}\\',
  '',
  '\footnotesize',
  '\begin{longtable}{@{}p{0.9cm}@{\hspace{0.15cm}}p{0.7cm}@{\hspace{0.15cm}}p{4.2cm}@{\hspace{0.15cm}}p{0.6cm}@{\hspace{0.15cm}}p{0.6cm}@{\hspace{0.15cm}}p{3.7cm}@{\hspace{0.15cm}}p{4.0cm}@{}}',
  '\toprule',
  'ID & Tipo & Enunciado & M & h & Justificacion & Criterio \\',
  '\midrule',
  '\endhead',
  '\bottomrule',
  '\endlastfoot',
  '\end{longtable}'
)
# Se inserta el cuerpo antes de \bottomrule.
$cuerpo = @()
foreach ($f in $filas) {
  $tipo = if ($f.tipo -like 'Calidad*') { 'Q' } else { 'F' }
  $cuerpo += '{0} & {1} & {2} & {3} & {4} & {5} & {6} \\' -f `
    (Esc $f.requisito), $tipo, (Esc $f.enunciado), `
    (Esc $f.moscow), (Esc $f.horas), (Esc $f.justificacion), (Esc $f.criterio_verificacion)
}
$lineas = $lineas[0..9] + $cuerpo + $lineas[10..($lineas.Count - 1)]
[IO.File]::WriteAllText($out, (($lineas -join "`n") + "`n"), $utf8)
"escrito: $out ($($cuerpo.Count) filas)"
