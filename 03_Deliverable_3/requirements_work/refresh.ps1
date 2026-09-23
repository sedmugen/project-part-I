$ErrorActionPreference='Stop'
$work='D:\BNU\SM7\FYP\03_Deliverable_3\requirements_work'
$path='D:\BNU\SM7\FYP\03_Deliverable_3\DailyKhata_Deliverable_3_v1.0.docx'
$word=New-Object -ComObject Word.Application
$word.Visible=$false
$word.DisplayAlerts=0
$word.Options.SaveNormalPrompt=$false
try {
 $doc=$word.Documents.Open($path,$false,$false)
 $doc.Content.LanguageID=2057
 $doc.Fields.Update() | Out-Null
 foreach($toc in $doc.TablesOfContents) { $toc.Update() }
 foreach($tof in $doc.TablesOfFigures) { $tof.Update() }
 $doc.Repaginate()
 $doc.Fields.Update() | Out-Null
 foreach($toc in $doc.TablesOfContents) { $toc.Update() }
 foreach($tof in $doc.TablesOfFigures) { $tof.Update() }
 $doc.Repaginate()
 $doc.Save()
 $doc.ExportAsFixedFormat((Join-Path $work 'D3_QA.pdf'),17)
 $spell=@()
 foreach($err in $doc.SpellingErrors) { $spell += $err.Text }
 [PSCustomObject]@{Pages=$doc.ComputeStatistics(2);SpellingFlags=($spell | Sort-Object -Unique);TOCs=$doc.TablesOfContents.Count;ListsOfTables=$doc.TablesOfFigures.Count} | ConvertTo-Json -Depth 5 | Set-Content -Encoding UTF8 (Join-Path $work 'word_qa.json')
 $doc.Close(0)
} finally { $word.Quit() }
Get-Content -LiteralPath (Join-Path $work 'word_qa.json')
