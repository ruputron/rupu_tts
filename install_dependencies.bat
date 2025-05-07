@echo off
setlocal

echo Checking Python version...
python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" > pyver.txt
set /p PYVER=<pyver.txt
del pyver.txt

if "%PYVER%" NEQ "3.10" if "%PYVER%" NEQ "3.11" (
    echo WARNING: Python is either not installed or "%PYVER%" is not officially supported.
    echo Please install Python 3.10 or 3.11 for best compatibility.
    pause
)

echo Installing required Python packages...
pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: Failed to install some dependencies.
    echo Please check the messages above and make sure your Python version is supported.
    pause
    exit /b 1
)

echo.
echo All dependencies installed successfully.
pause