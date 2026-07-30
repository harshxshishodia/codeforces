#Requires -Version 5.1
# Fix: re-fetch problems pages, extract only sample tests with proper newlines
$rootDir = "D:\codeforces\0001-0100"
$agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
$tmp = "$env:TEMP\cf_fix.html"

function Strip-Tags {
    param($Text)
    $plain = $Text -replace '<[^>]+>', ' '
    $plain = $plain -replace '&nbsp;', ' '; $plain = $plain -replace '&lt;', '<'
    $plain = $plain -replace '&gt;', '>'; $plain = $plain -replace '&amp;', '&'
    $plain = $plain -replace '&quot;', '"'; $plain = $plain -replace '&#39;', "'"
    $plain = $plain -replace '&minus;', '-'; $plain = $plain -replace '&le;', '<='
    $plain = $plain -replace '&ge;', '>='; $plain = $plain -replace '&rarr;', '->'
    $plain = $plain -replace '&mdash;', '--'; $plain = $plain -replace '&times;', 'x'
    $plain = $plain -replace '&dash;', '-'; $plain = $plain -replace '&gt;', '>'
    $plain = $plain -replace '&lt;', '<'
    # Remove &#xxxx; numeric entities
    $plain = $plain -replace '&#\d+;', ' '; $plain = $plain -replace '&#x[0-9a-fA-F]+;', ' '
    # Collapse horizontal whitespace only (not newlines)
    $plain = $plain -replace '[ \t]+', ' '
    return $plain.Trim()
}

function Get-PreText {
    param($PreHtml)
    $text = $PreHtml -replace '<br\s*/?>', "`n"
    $text = Strip-Tags $text
    return $text.Trim()
}

$fixed = 0; $errors = @()
foreach ($cid in 1..100) {
    Write-Host "C$cid... " -NoNewline
    curl.exe -s -L --max-time 20 --retry 3 --retry-delay 3 -H "User-Agent: $agent" -H "Accept: text/html,application/xhtml+xml" -H "Accept-Language: en-US,en;q=0.9" -H "Referer: https://codeforces.com/" -o $tmp "https://codeforces.com/contest/${cid}/problems" 2>$null
    $bytes = [System.IO.File]::ReadAllBytes($tmp); $html = [System.Text.Encoding]::UTF8.GetString($bytes)
    if ($html -match 'Just a moment' -or $html.Length -lt 1000) { Write-Host "BLOCKED" -ForegroundColor Red; $errors += $cid; Start-Sleep 5000; continue }

    $parts = $html -split '<div class="problem-statement">'
    if ($parts.Count -le 1) { Write-Host "FAIL" -ForegroundColor Red; $errors += $cid; Start-Sleep 5000; continue }

    $found = 0
    for ($i = 1; $i -lt $parts.Count; $i++) {
        $chunk = $parts[$i]
        $titleM = [regex]::Match($chunk, '(?s)<div class="title">(.*?)</div>')
        if (-not $titleM.Success) { continue }
        $titleText = ($titleM.Groups[1].Value -replace '<[^>]+>', '').Trim()
        $letter = ($titleText -split '\.')[0].Trim()
        if (-not $letter) { continue }

        $readme = Join-Path -Path $rootDir -ChildPath "*" | Resolve-Path | Get-ChildItem -Directory | ForEach-Object {
            $c = [int](($_.Name -split ' - ')[0]); if ($c -eq $cid) { $_ }
        } | ForEach-Object {
            Get-ChildItem -LiteralPath $_.FullName -Directory | Where-Object { ($_.Name -split ' - ')[0] -eq $letter }
        } | ForEach-Object { Join-Path -Path $_.FullName -ChildPath 'README.md' }

        if (-not $readme -or -not (Test-Path $readme)) { continue }

        # Read existing README
        $oldBytes = [System.IO.File]::ReadAllBytes($readme); $oldText = [System.Text.Encoding]::UTF8.GetString($oldBytes)

        # Extract sample tests correctly from chunk
        $parts3 = @(); $idx = 0
        foreach ($tm in [regex]::Matches($chunk, '(?s)<div class="sample-test">.*?<div class="input">.*?<pre>(.*?)</pre>.*?<div class="output">.*?<pre>(.*?)</pre>.*?</div>')) {
            $idx++; $inT = Get-PreText $tm.Groups[1].Value; $outT = Get-PreText $tm.Groups[2].Value
            $parts3 += "Example ${idx}:"; $parts3 += '```'; $parts3 += $inT; $parts3 += '```'; $parts3 += '```'; $parts3 += $outT; $parts3 += '```'
        }
        if ($parts3.Count -eq 0) { continue }

        $newExamples = $parts3 -join "`n"

        # Replace the Examples section in the existing README
        $exampleMatch = [regex]::Match($oldText, '(?s)(## Examples\n+)(.*?)(\n+## (Note|$))')
        if ($exampleMatch.Success) {
            $prefix = $exampleMatch.Groups[1].Value
            $suffix = $exampleMatch.Groups[3].Value
            $newText = $oldText.Substring(0, $exampleMatch.Index) + $prefix + $newExamples + $suffix + $oldText.Substring($exampleMatch.Index + $exampleMatch.Length)
            [System.IO.File]::WriteAllBytes($readme, [System.Text.Encoding]::UTF8.GetBytes($newText))
            $found++
        }
    }
    $fixed += $found
    Write-Host "$found fixed" -ForegroundColor Green
    Start-Sleep -Milliseconds 3000
}
Write-Host "`nDone! Fixed: $fixed | Errors: $($errors.Count)" -ForegroundColor Cyan
if ($errors.Count -gt 0) { $errors | ForEach-Object { Write-Host "  C$_" -ForegroundColor Red } }
