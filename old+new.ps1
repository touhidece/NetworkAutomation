$LocalUsers = (Get-ChildItem -Path "C:\Users").Name

function Stop-FirefoxProcesses {
    param (
        [string]$processName
    )
    $runningProcess = Get-Process -Name $processName -ErrorAction SilentlyContinue
    if ($runningProcess) {
        try {
            Stop-Process -Name $processName -Force -ErrorAction Stop
            Write-Host "Stopped $processName process."
        }
        catch {
            Write-Warning "Failed to stop $processName process: $($_.Exception.Message)"
        }
    }
}

Stop-FirefoxProcesses -processName "firefox"
Stop-FirefoxProcesses -processName "firefox.exe"

# Uninstalling from Program Files
if (Test-Path "${env:ProgramFiles(x86)}\Mozilla Firefox\uninstall\helper.exe"){
    Start-Process -FilePath "${env:ProgramFiles(x86)}\Mozilla Firefox\uninstall\helper.exe" -ArgumentList '/S' -Wait
}
if (Test-Path "${env:ProgramFiles}\Mozilla Firefox\uninstall\helper.exe"){
    Start-Process -FilePath "${env:ProgramFiles}\Mozilla Firefox\uninstall\helper.exe" -ArgumentList '/S' -Wait
}

# Uninstalling for each user
ForEach ($LocalUser in $LocalUsers){
    $Userpath = "C:\Users\" + $LocalUser
    $firefoxPath = "$Userpath\AppData\Local\Mozilla Firefox\uninstall\helper.exe"
    $oldFirefoxPath = "$Userpath\AppData\Local\Mozilla\Firefox\uninstall\helper.exe"
    if (Test-Path $firefoxPath) {
        Start-Process -FilePath $firefoxPath -ArgumentList '/S' -Wait
    }
    elseif (Test-Path $oldFirefoxPath) {
        Start-Process -FilePath $oldFirefoxPath -ArgumentList '/S' -Wait
    }

    Start-Sleep 20

    $mozillaPath = "$Userpath\AppData\Local\Mozilla"
    $oldMozillaPath = "$Userpath\AppData\Local\Mozilla\Firefox"
    $roamingMozillaPath = "$Userpath\AppData\Roaming\Mozilla"
    $roamingMicrosoftPath = "$Userpath\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Firefox.lnk"
    $desktopPath = "$Userpath\desktop\firefox.lnk"

    Remove-Item -Path $mozillaPath -Force -Recurse -Verbose
    Remove-Item -Path $oldMozillaPath -Force -Recurse -Verbose
    Remove-Item -Path $roamingMozillaPath -Force -Recurse -Verbose
    Remove-Item -Path $roamingMicrosoftPath -Force -Verbose
    Remove-Item -Path $desktopPath -Force -Verbose
}

# Remove related registry keys
$pathToRemove = @(
    'HKLM:\Software\Mozilla',
    'HKLM:\SOFTWARE\mozilla.org',
    'HKLM:\SOFTWARE\MozillaPlugins',
    'HKLM:\SOFTWARE\WOW6432Node\Mozilla',
    'HKLM:\SOFTWARE\WOW6432Node\mozilla.org',
    'HKLM:\SOFTWARE\WOW6432Node\MozillaPlugins',
    'HKCU:\SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\UNINSTALL\Mozilla Firefox*',
    'HKCU:\Software\Mozilla',
    'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox.lnk'
)

foreach($path in $pathToRemove) {
    if(Test-Path $path) {
        try {
            Write-Verbose "Attempting to remove: $path"
            Remove-Item $path -Recurse -Force
            Write-Verbose "Successfully removed: $path"
        }
        catch {
            Write-Warning $_.Exception.Message
        }
    }
}
