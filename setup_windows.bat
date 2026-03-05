<# : setup_windows.bat
@echo off
copy /y "%~f0" "%TEMP%\setup_oop.ps1" >nul
powershell -NoProfile -ExecutionPolicy Bypass -File "%TEMP%\setup_oop.ps1"
del "%TEMP%\setup_oop.ps1" >nul 2>nul
pause
exit /b
#>

# ==============================================================
#  OOP 2026 - One-click Environment Setup (Windows)
#
#  This script:
#    1. Downloads and installs Miniconda
#    2. Sets PATH environment variable
#    3. Creates conda env (OOP) and installs packages
#    4. Git clones the practice repository
#    5. Runs environment verification tests
#
#  Usage: Double-click setup_windows.bat
# ==============================================================

Write-Host ""
Write-Host "=================================================="
Write-Host "  OOP 2026 Environment Setup"
Write-Host "=================================================="
Write-Host ""

$installDir   = "$env:USERPROFILE\miniconda3"
$envName      = "OOP"
$pythonVer    = "3.9"
$repoUrl      = "https://github.com/ElionLAB/OOP_2026_Practice.git"
$workDir      = "$env:USERPROFILE\OOP_2026_Practice"
$condaExe     = "$installDir\Scripts\conda.exe"
$envPython    = "$installDir\envs\$envName\python.exe"
$minicondaUrl = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
$installer    = "$env:TEMP\Miniconda3-latest-Windows-x86_64.exe"

# ---- Step 1: Install Miniconda ----
Write-Host "[1/5] Checking Miniconda..."

if (Test-Path $condaExe) {
    Write-Host "      - Already installed. Skipping."
} else {
    Write-Host "      - Downloading Miniconda (this may take a few minutes)..."
    try {
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
        (New-Object Net.WebClient).DownloadFile($minicondaUrl, $installer)
    } catch {
        Write-Host "[ERROR] Download failed: $_"
        Write-Host "        Check your internet connection."
        return
    }

    Write-Host "      - Installing Miniconda (silent mode)..."
    $proc = Start-Process -Wait -PassThru -FilePath $installer -ArgumentList "/InstallationType=JustMe", "/RegisterPython=0", "/AddToPath=0", "/S", "/D=$installDir"
    if ($proc.ExitCode -ne 0) {
        Write-Host "[ERROR] Miniconda installation failed."
        return
    }
    Remove-Item $installer -Force -ErrorAction SilentlyContinue
    Write-Host "      - Done."
}

# ---- Step 2: Set PATH ----
Write-Host ""
Write-Host "[2/5] Setting PATH..."

$condaPaths = "$installDir;$installDir\Scripts;$installDir\condabin;$installDir\Library\bin"
$env:PATH = "$condaPaths;$env:PATH"

$ver = & $condaExe --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] conda not working. Check installation."
    return
}
Write-Host "      - $ver"

$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($userPath -and $userPath -like "*miniconda3*") {
    Write-Host "      - conda PATH already registered."
} else {
    if ($userPath) { $newPath = "$condaPaths;$userPath" } else { $newPath = $condaPaths }
    [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
    Write-Host "      - Registered conda in user PATH."
}

# ---- Step 3: Conda env + packages ----
Write-Host ""
Write-Host "[3/5] Setting up conda env ($envName)..."

# Accept conda ToS for default channels (required since conda 26.x)
$tosChannels = @(
    "https://repo.anaconda.com/pkgs/main",
    "https://repo.anaconda.com/pkgs/r",
    "https://repo.anaconda.com/pkgs/msys2"
)
foreach ($ch in $tosChannels) {
    & $condaExe tos accept --override-channels --channel $ch 2>&1 | Out-Null
}

if (Test-Path $envPython) {
    Write-Host "      - Env already exists."
} else {
    Write-Host "      - Creating env (Python $pythonVer)..."
    & $condaExe create -n $envName python=$pythonVer -y -q 2>&1 | Out-Host
    if (-not (Test-Path $envPython)) {
        Write-Host "[ERROR] Failed to create conda env."
        return
    }
}

# Check core packages
& $condaExe run -n $envName python -c "import pytest, bs4, PIL" 2>$null | Out-Null
if ($LASTEXITCODE -eq 0) {
    Write-Host "      - Core packages already installed."
} else {
    Write-Host "      - Installing packages (beautifulsoup4, pytest, pillow, ipykernel)..."
    & $condaExe install -n $envName beautifulsoup4 pytest pillow ipykernel -y -q 2>&1 | Out-Host
}

# git
& $condaExe run -n $envName git --version 2>$null | Out-Null
if ($LASTEXITCODE -eq 0) {
    Write-Host "      - git already installed."
} else {
    Write-Host "      - Installing git..."
    & $condaExe install -n $envName git -y -q 2>&1 | Out-Host
}

# tox
& $condaExe run -n $envName python -c "import tox" 2>$null | Out-Null
if ($LASTEXITCODE -eq 0) {
    Write-Host "      - tox already installed."
} else {
    Write-Host "      - Installing tox..."
    & $condaExe run -n $envName pip install tox -q 2>&1 | Out-Host
}

Write-Host "      - Registering Jupyter kernel..."
& $condaExe run -n $envName python -m ipykernel install --user --name $envName --display-name "Python 3 (OOP)" 2>&1 | Out-Null

# ---- Step 4: Clone repository ----
Write-Host ""
Write-Host "[4/5] Cloning repository..."

$gitCmd = "$installDir\envs\$envName\Library\bin\git.exe"
if (-not (Test-Path $gitCmd)) { $gitCmd = "git" }

if (Test-Path "$workDir\.git") {
    Write-Host "      - Repository exists. Pulling latest..."
    Push-Location $workDir
    $pullOutput = & $gitCmd pull origin main 2>&1
    $pullOutput | ForEach-Object { Write-Host "      $_" }
    Pop-Location
} elseif (Test-Path $workDir) {
    Write-Host "      - Folder exists but not a git repo. Check: $workDir"
} else {
    Write-Host "      - Cloning..."
    & $gitCmd clone $repoUrl $workDir 2>&1 | Out-Host
    if (-not (Test-Path "$workDir\.git")) {
        Write-Host "[ERROR] Git clone failed."
        return
    }
}

# ---- Step 5: Run tests ----
Write-Host ""
Write-Host "[5/5] Running tests..."
Write-Host ""

Push-Location $workDir
$env:PYTHONIOENCODING = "utf-8"
& $condaExe run --no-capture-output -n $envName python tests/test_setup.py
$testResult = $LASTEXITCODE
Pop-Location

Write-Host ""
if ($testResult -eq 0) {
    Write-Host "=================================================="
    Write-Host "  Setup completed successfully."
    Write-Host "=================================================="
    Write-Host ""
    Write-Host "  Next steps:"
    Write-Host "    1. Open folder in VSCode: $workDir"
    Write-Host "    2. Ctrl+Shift+P > Python: Select Interpreter"
    Write-Host "       Select: Python 3.9.x ('OOP': conda)"
    Write-Host "    3. In terminal: conda activate OOP"
} else {
    Write-Host "=================================================="
    Write-Host "  Setup finished but some tests failed."
    Write-Host "  Check the output above."
    Write-Host "=================================================="
}
Write-Host ""
