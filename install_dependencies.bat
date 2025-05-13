@echo off
echo ==========================================
echo Setting up Rupu TTS dependencies...
echo ==========================================
echo.

:: Ensure Python is installed and accessible
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python 3.10+ from https://www.python.org/downloads/
    echo Continuing, but some installations may fail...
    set PYTHON_ERROR=1
)

:: Upgrade pip, setuptools, and wheel
echo Upgrading pip, setuptools, and wheel...
python -m pip install --upgrade pip setuptools wheel >upgrade_log.txt 2>&1
if %errorlevel% neq 0 (
    echo WARNING: Failed to upgrade pip, setuptools, or wheel.
    echo Check upgrade_log.txt for details.
    set PIP_ERROR=1
)

:: Check for Microsoft C++ Build Tools
where cl >nul 2>&1
if %errorlevel% neq 0 (
    echo WARNING: Microsoft C++ Build Tools not found.
    echo Downloading and installing minimal required components...

    :: Download Build Tools installer
    powershell -Command "& {Invoke-WebRequest -Uri 'https://aka.ms/vs/17/release/vs_BuildTools.exe' -OutFile 'vs_BuildTools.exe'}" >build_tools_log.txt 2>&1

    :: Run the installer silently
    if exist vs_BuildTools.exe (
        echo Running Build Tools installer...
        start /wait vs_BuildTools.exe --quiet --wait --norestart --add Microsoft.VisualStudio.Workload.VCTools >build_tools_log.txt 2>&1
        del vs_BuildTools.exe
    ) else (
        echo ERROR: Failed to download Build Tools installer.
        echo Check build_tools_log.txt for details.
        set BUILD_TOOLS_ERROR=1
    )

    echo Build Tools installation attempted. Continuing...
)

:: Install dependencies
echo Installing dependencies from requirements.txt...
python -m pip install -r requirements.txt >install_log.txt 2>&1
if %errorlevel% neq 0 (
    echo WARNING: Failed to install dependencies.
    echo Check install_log.txt for details.
    set DEPENDENCIES_ERROR=1
)

:: Install TTS with no build isolation (avoids wheel issues)
echo Installing Coqui TTS...
python -m pip install TTS --no-build-isolation >tts_log.txt 2>&1
if %errorlevel% neq 0 (
    echo WARNING: Failed to install Coqui TTS.
    echo Check tts_log.txt for details.
    set TTS_ERROR=1
)

:: Install PyWorld separately (if needed)
echo Installing PyWorld...
python -m pip install pyworld >pyworld_log.txt 2>&1
if %errorlevel% neq 0 (
    echo WARNING: Failed to install PyWorld.
    echo Check pyworld_log.txt for details.
    set PYWORLD_ERROR=1
)

echo.
echo ==========================================
echo Setup complete! Checking for errors...
echo ==========================================
echo.

:: Display summary of issues
if defined PYTHON_ERROR echo - Python installation issue detected.
if defined PIP_ERROR echo - Pip upgrade failed.
if defined BUILD_TOOLS_ERROR echo - Microsoft C++ Build Tools were missing but failed to install.
if defined DEPENDENCIES_ERROR echo - Some dependencies failed to install.
if defined TTS_ERROR echo - Coqui TTS installation failed.
if defined PYWORLD_ERROR echo - PyWorld installation failed.

echo.
echo If any errors occurred, check the log files for details.
echo You may need to manually fix some issues before running Rupu TTS.
echo ==========================================
pause
