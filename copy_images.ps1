$webDir = "c:\Users\User\Downloads\SEO-20260506T052936Z-3-001\SEO\web4"
$brainDir = "C:\Users\User\.gemini\antigravity\brain\45502dd0-97b4-427b-a3c4-e2c3b9d4b136"

# Copy images
$imagePrefixes = @("logo", "product_1", "product_2", "product_3", "product_4", "product_5")
$availableProducts = @()

foreach ($prefix in $imagePrefixes) {
    $files = Get-ChildItem -Path "$brainDir\${prefix}_*.png" | Sort-Object LastWriteTime -Descending
    if ($files.Count -gt 0) {
        $src = $files[0].FullName
        $dst = Join-Path $webDir "$prefix.png"
        Copy-Item -Path $src -Destination $dst -Force
        if ($prefix -ne "logo") {
            $availableProducts += $prefix
        }
    }
}

# Fill missing 6-16
for ($i = 6; $i -le 16; $i++) {
    if ($availableProducts.Count -gt 0) {
        $idx = ($i - 6) % $availableProducts.Count
        $srcPrefix = $availableProducts[$idx]
        $srcPath = Join-Path $webDir "$srcPrefix.png"
        $dstPath = Join-Path $webDir "product_$i.png"
        if (Test-Path $srcPath) {
            Copy-Item -Path $srcPath -Destination $dstPath -Force
        }
    }
}

Write-Output "Images copied successfully."
