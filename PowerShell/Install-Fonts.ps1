#Change font folder to the destination the fonts live in.
    param(
        [string]$FontFolder = ""
    )
    
    try {
        $FontItem = Get-Item -Path $FontFolder
    } catch{
        Write-Host "Unable to find folder $FontFolder"
        exit(1)
    }

    $FontList = Get-ChildItem -Path "$FontItem\*" -Include ('*.fon','*.otf','*.ttc','*.ttf')
 
    foreach ($Font in $FontList) 
    {
        Copy-Item $Font "C:\Windows\Fonts"
        New-ItemProperty -Name $Font.BaseName -Path "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Fonts" -PropertyType string -Value $Font.name         
    }
