@echo off
:: Build Rupu TTS into a standalone .exe with custom icon and taskbar name
pyinstaller --onefile --windowed --icon=appicon.ico --name="Rupu TTS" rupu_tts.py
echo.
echo ✅ Build complete. The executable is located in the 'dist' folder.
pause
