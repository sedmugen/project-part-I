param([string]$Pattern='*v2.0.docx')
$ErrorActionPreference='Stop'
$root='D:\BNU\SM7\FYP'
$out=Join-Path $root '00_Project_Governance\reconstruction_work\rendered'
New-Item -ItemType Directory -Path $out -Force | Out-Null
$word=New-Object -ComObject Word.Application
$word.Visible=$false
$word.DisplayAlerts=0
$word.Options.SaveNormalPrompt=$false
try {
 $files=Get-ChildItem -LiteralPath $root -Recurse -File -Filter $Pattern | Where-Object { $_.DirectoryName -notlike '*reconstruction_work*' -and $_.Name -notlike '*v1.0*' -and $_.Name -notlike 'dailykhata-d1.docx' }
 foreach($file in $files) {
  Write-Output ('Opening '+$file.Name)
  $doc=$word.Documents.Open($file.FullName,$false,$false)
  Write-Output 'Updating fields'
  $doc.Content.LanguageID=2057
  $doc.Fields.Update() | Out-Null
  foreach($toc in $doc.TablesOfContents) { $toc.Update() }
  foreach($tof in $doc.TablesOfFigures) { $tof.Update() }
  $doc.Repaginate()
  $doc.Fields.Update() | Out-Null
  foreach($toc in $doc.TablesOfContents) { $toc.Update() }
  $doc.Repaginate()
  $doc.Save()
  Write-Output 'Exporting PDF'
  $pdf=Join-Path $out ($file.BaseName+'.pdf')
  $doc.ExportAsFixedFormat($pdf,17)
  $spell=@()
  foreach($err in $doc.SpellingErrors) { $spell += $err.Text }
  [PSCustomObject]@{File=$file.Name;Pages=$doc.ComputeStatistics(2);SpellingFlags=($spell | Sort-Object -Unique)} | ConvertTo-Json -Depth 4 | Set-Content -Encoding UTF8 (Join-Path $out ($file.BaseName+'_word.json'))
  $doc.Close(0)
  Write-Output $pdf
 }
} finally { $word.Quit() }
