@echo off
setlocal ENABLEEXTENSIONS

echo Checking for Python in PATH...
where python >nul 2>&1
if errorlevel 1 (
    echo.
    echo Python executable not found in PATH.
    echo Please install Python 3.10 from https://www.python.org/downloads/
    echo and make sure to check “Add Python to PATH” during installation.
    pause
    exit /b 1
)

:: Retrieve major.minor version
for /f "delims=" %%V in ('python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"') do set PYVER=%%V

echo Detected Python version %PYVER%.

if not "%PYVER%"=="3.10" (
    echo.
    echo Unsupported Python version: %PYVER%.
    echo Rupu TTS requires Python 3.10 only.
    pause
    exit /b 1
)

echo.
echo Python 3.10 is accessible in PATH.
echo Proceeding with dependency installation...

python -m pip install --upgrade pip
if errorlevel 1 (
    echo.
    echo Failed to upgrade pip.
    pause
    exit /b 1
)

python -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies.
    pause
    exit /b 1
)

echo.
echo All dependencies installed successfully.
echo You can now run the application with:
echo     python rupu_tts.py
pause
exit /b 0
