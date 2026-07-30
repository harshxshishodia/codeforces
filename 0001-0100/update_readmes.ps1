#Requires -Version 5.1
$rootDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

function Strip-Html {
    param($Text)
    $plain = $Text -replace '<[^>]+>', ' '
    $plain = $plain -replace '&nbsp;', ' '; $plain = $plain -replace '&lt;', '<'
    $plain = $plain -replace '&gt;', '>'; $plain = $plain -replace '&amp;', '&'
    $plain = $plain -replace '&quot;', '"'; $plain = $plain -replace '&#39;', "'"
    $plain = $plain -replace '&minus;', '-'; $plain = $plain -replace '&le;', '<='
    $plain = $plain -replace '&ge;', '>='; $plain = $plain -replace '&rarr;', '->'
    $plain = $plain -replace '&mdash;', '--'; $plain = $plain -replace '&times;', 'x'
    $plain = $plain -replace '&#\d+;', ' '; $plain = $plain -replace '&#x[0-9a-fA-F]+;', ' '
    $plain = $plain -replace '[ \t]+', ' '; return $plain.Trim()
}

function Format-Text {
    param($Html)
    $text = $Html -replace '<br\s*/?>', "`n"
    $text = $text -replace '</?p>', "`n"; $text = $text -replace '<li>', "`n- "
    $text = $text -replace '</li>', ''; $text = $text -replace '</?[ou]l>', "`n"
    $text = Strip-Html $text
    $text = $text -replace "`n`n`n+", "`n`n"; return $text.Trim()
}

# Build problem map
$problemMap = @{}
Get-ChildItem -LiteralPath $rootDir -Directory | ForEach-Object {
    $cid = [int](($_.Name -split ' - ')[0])
    Get-ChildItem -LiteralPath $_.FullName -Directory | ForEach-Object {
        $letter = ($_.Name -split ' - ')[0]
        $problemMap["${cid}_${letter}"] = Join-Path -Path $_.FullName -ChildPath 'README.md'
    }
}

$processed = 0; $errors = @(); $counter = 0

foreach ($cid in 1..100) {
    $counter++
    Write-Host "[$counter/100] Contest $cid... " -NoNewline

    $url = "https://codeforces.com/contest/${cid}/problems"
    $html = curl.exe -s -L --max-time 20 --retry 3 --retry-delay 3 `
        -H "User-Agent: $agent" -H "Accept: text/html,application/xhtml+xml" `
        -H "Accept-Language: en-US,en;q=0.9" -H "Referer: https://codeforces.com/" `
        $url

    if (-not $html -or $html -match 'Just a moment') {
        Write-Host "FAIL (blocked)" -ForegroundColor Red
        $errors += "C${cid}: blocked"; Start-Sleep 5000; continue
    }

    # Split by problem-statement divs - more robust pattern
    $parts = $html -split '<div class="problem-statement">'
    if ($parts.Count -le 1) { Write-Host "FAIL (no stmts)" -ForegroundColor Red; $errors += "C${cid}: no stmts"; Start-Sleep 5000; continue }

    $found = 0
    for ($i = 1; $i -lt $parts.Count; $i++) {
        $chunk = $parts[$i]

        # Get title and letter
        $titleM = [regex]::Match($chunk, '(?s)<div class="title">(.*?)</div>')
        if (-not $titleM.Success) { continue }
        $titleText = Strip-Html $titleM.Groups[1].Value
        $letter = ($titleText -split '\.')[0].Trim()
        if (-not $letter) { continue }

        $readme = $problemMap["${cid}_${letter}"]
        if (-not $readme) { continue }

        $time = ''; $m = [regex]::Match($chunk, '(?s)<div class="time-limit">.*?<div class="property-title">.*?</div>(.*?)</div>')
        if ($m.Success) { $time = Strip-Html $m.Groups[1].Value }

        $mem = ''; $m = [regex]::Match($chunk, '(?s)<div class="memory-limit">.*?<div class="property-title">.*?</div>(.*?)</div>')
        if ($m.Success) { $mem = Strip-Html $m.Groups[1].Value }

        $stmtText = ''; $m = [regex]::Match($chunk, '(?s)</div>\s*<div>(.*?)</div>\s*<div class="input-specification"')
        if ($m.Success) { $stmtText = Format-Text $m.Groups[1].Value }

        $inputSpec = ''; $m = [regex]::Match($chunk, '(?s)<div class="input-specification">(.*?)</div>\s*<div class="output-specification"')
        if ($m.Success) { $inputSpec = Format-Text $m.Groups[1].Value; $inputSpec = $inputSpec -replace '^Input\s*', '' }

        $outputSpec = ''; $m = [regex]::Match($chunk, '(?s)<div class="output-specification">(.*?)</div>\s*<div class="sample-tests"')
        if ($m.Success) { $outputSpec = Format-Text $m.Groups[1].Value; $outputSpec = $outputSpec -replace '^Output\s*', '' }

        $sampleTests = ''; $parts2 = @(); $idx = 0
        foreach ($tm in [regex]::Matches($chunk, '(?s)<div class="sample-test">.*?<div class="input">.*?<pre>(.*?)</pre>.*?<div class="output">.*?<pre>(.*?)</pre>.*?</div>')) {
            $idx++
            $inT = $tm.Groups[1].Value -replace '<br\s*/?>', "`n"; $inT = $inT -replace '<[^>]+>', ''; $inT = $inT.Trim()
            $outT = $tm.Groups[2].Value -replace '<br\s*/?>', "`n"; $outT = $outT -replace '<[^>]+>', ''; $outT = $outT.Trim()
            $parts2 += "Example ${idx}:"; $parts2 += '```'; $parts2 += $inT; $parts2 += '```'; $parts2 += '```'; $parts2 += $outT; $parts2 += '```'
        }
        if ($parts2.Count -gt 0) { $sampleTests = $parts2 -join "`n" }

        $note = ''; $m = [regex]::Match($chunk, '(?s)<div class="note">(.*?)</div>\s*</div>')
        if ($m.Success) { $note = Format-Text $m.Groups[1].Value; $note = $note -replace '^Note\s*', '' }

        $lines = @()
        $lines += "# ${titleText}"
        $lines += ''; $lines += "**Submission:** https://codeforces.com/contest/${cid}/problem/${letter}"
        $lines += ''; $lines += "**Limits:** ${time} / ${mem}"
        $lines += ''; $lines += '## Problem Statement'; $lines += ''; $lines += $stmtText
        $lines += ''; $lines += '## Input'; $lines += ''; $lines += $inputSpec
        $lines += ''; $lines += '## Output'; $lines += ''; $lines += $outputSpec
        $lines += ''; $lines += '## Examples'; $lines += ''
        if ($sampleTests) { $lines += $sampleTests } else { $lines += '(none)' }
        if ($note) { $lines += ''; $lines += '## Note'; $lines += ''; $lines += $note }

        Set-Content -Path $readme -Value ($lines -join "`n") -Encoding UTF8
        $found++
    }

    $processed += $found
    Write-Host "$found problems" -ForegroundColor Green
    Start-Sleep -Milliseconds 3000
}

Write-Host "`nDone! Updated: $processed | Errors: $($errors.Count)" -ForegroundColor Cyan
if ($errors.Count -gt 0) { $errors | ForEach-Object { Write-Host "  $_" -ForegroundColor Red } }
