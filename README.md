# Rupu TTS

**Rupu TTS** is a lightweight, open-source, and offline-capable text-to-speech (TTS) application built on [Coqui TTS](https://github.com/coqui-ai/TTS). It offers a simple desktop interface to generate speech in `.wav`, `.mp3`, or `.flac` formats — no internet connection required after initial setup.

---

## 🛠 Designed to be built on

- Easily buld your own version from source
- Potential for many improvements
- Easier introduction to open-source for beginners

## 🔧 Features

- 🗣️ Built on Coqui TTS (fully open-source, offline engine)
- 🎛️ Simple, user-friendly desktop GUI (Tkinter)
- 🎧 Output formats: `.wav`, `.mp3`, and `.flac`
- 💻 Build your own standalone Windows `.exe`
- 🚫 No telemetry or data collection
- 🪶 Lightweight, portable, no installer needed

---

## ✅ Requirements

- **Windows 10 or 11**
- **Python 3.10**
- Ensure you check **“Add Python to PATH”** when installing Python
- Optional: [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)  
  (some dependencies may require it on clean systems)

---

## 📥 Installation

### 1. Clone the Repository with git or download a release

```bash
git clone https://github.com/yourusername/rupu_tts.git
cd rupu_tts

2. Install Dependencies

Run the setup script (Windows only):

install.py

This will:

    Confirm that Python 3.10 is installed and in PATH

    Install all required Python packages from requirements.txt

    Notify you if additional system dependencies are missing
	

🛠 Build a Standalone .exe 

To create a self-contained .exe:

build_rupu_tts.bat

    Output will be saved in the dist/ folder

    No Python installation required on target machine

## 📁 Project Structure
File / Folder	Description
rupu_tts.py	Main Python GUI application
install_dependencies.bat	Windows script to install dependencies
build_rupu_tts.bat	Build script for creating .exe
requirements.txt	Python dependency list
README.md	This file
appicon.ico	App icon for EXE builds (optional)
.gitignore	Git ignore rules
LICENSE	MIT license
🙋 Contributing

Pull requests, bug reports, and suggestions are welcome!
To contribute:

    Fork the repo

    Create a feature or fix branch

    Make your changes

    Submit a pull request

💖 Support This Project

If you’d like to support the development of Rupu TTS:

👉 https://ko-fi.com/rupsiedaisy
📜 License

Rupu TTS is released under the MIT License.
🙏 Credits

    Core engine: Coqui TTS

    GUI design and packaging by [Rupu]
