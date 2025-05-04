@echo off
setlocal

:: Optional: Path to the Python installer
set PYTHON_INSTALLER=python-3.11.8-amd64.exe

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Installing Python...
    if exist "%PYTHON_INSTALLER%" (
        "%PYTHON_INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    ) else (
        echo Python installer not found. Please place %PYTHON_INSTALLER% in this folder.
        pause
        exit /b
    )
)

:: Upgrade pip
python -m ensurepip --upgrade
python -m pip install --upgrade pip

:: Install dependencies
echo Installing required Python packages...
python -m pip install TTS

:: Done
echo.
echo All dependencies installed successfully.
echo Press any key to continue...
pause >nul
endlocal
