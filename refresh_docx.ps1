# PowerShell script to update fields, refresh TOC and page numbers, and export PDF
$exports = @(
    "DailyKhata_Deliverable_1.docx",
    "DailyKhata_Deliverable_2.docx",
    "DailyKhata_Deliverable_3.docx"
)

$repoDir = (Get-Location).Path
$exportsDir = Join-Path $repoDir "exports"

Write-Output "Starting Microsoft Word COM Automation..."
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

try {
    foreach ($file in $exports) {
        $docxPath = Join-Path $exportsDir $file
        $pdfPath = [System.IO.Path]::ChangeExtension($docxPath, ".pdf")
        Write-Output "Processing $file..."
        
        $doc = $word.Documents.Open($docxPath)
        
        # Update main story fields (including TOC)
        $doc.Fields.Update()
        
        # Update headers and footers across all sections
        foreach ($section in $doc.Sections) {
            foreach ($hdr in $section.Headers) {
                if ($hdr.Exists) {
                    $hdr.Range.Fields.Update()
                }
            }
            foreach ($ftr in $section.Footers) {
                if ($ftr.Exists) {
                    $ftr.Range.Fields.Update()
                }
            }
        }
        
        # Repaginate to compute final page numbers
        $doc.Repaginate()
        $pageCount = $doc.ComputeStatistics([Microsoft.Office.Interop.Word.WdStatistic]::wdStatisticPages)
        Write-Output "  Page count for ${file}: $pageCount"
        
        # Save updated DOCX
        $doc.Save()
        
        # Export PDF for visual inspection
        $doc.ExportAsFixedFormat($pdfPath, 17) # 17 = wdExportFormatPDF
        Write-Output "  Exported PDF: $pdfPath"
        
        $doc.Close()
    }
}
finally {
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
    Write-Output "Word COM closed cleanly."
}
