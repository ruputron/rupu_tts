
# 🗣️ Rupu TTS

**Rupu TTS** is a lightweight, portable, and open-source desktop **text-to-speech** (TTS) app powered by [Coqui TTS](https://github.com/coqui-ai/TTS). It offers a simple, offline-friendly way to generate natural-sounding speech from text — with zero internet dependency.

---

## ✨ Features

- 🧠 Built on the Coqui TTS engine (offline, open-source)
- 🖥️ Clean, intuitive desktop GUI
- 🔊 Output to `.wav`, `.mp3`, and `.flac` formats
- 🛠️ Easily build your own Windows `.exe`
- 🪶 Lightweight and portable (no installer needed)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rupu_tts.git
cd rupu_tts
```

### 2. Install Dependencies (Windows)

You can use the provided batch script:

```bat
install_dependencies.bat
```

Or manually install via pip:

```bash
pip install -r requirements.txt
```

> ⚠️ Python 3.10 or later is recommended.

---

## 🖥️ Usage

### Run the app:

```bash
python rupu_tts.py
```

Enter your text, choose your options, and click play or export. Outputs include:
- 🔉 Direct playback
- 💾 Saved files in `.mp3`, `.flac`, or `.wav` format

---

## 🛠️ Building an `.exe` (Optional)

You can turn your local Python script into a standalone `.exe` using the included build script:

```bat
build_rupu_tts.bat
```

This uses `pyinstaller` to create a self-contained binary. Output will appear in the `dist/` folder.

> 🔒 No external network calls or telemetry — everything runs locally.

---

## 📁 File Overview

| File / Folder           | Purpose                                   |
|-------------------------|-------------------------------------------|
| `rupu_tts.py`           | Main app script                           |
| `install_dependencies.bat` | One-click dependency installer         |
| `build_rupu_tts.bat`    | Script to generate `.exe`                 |
| `appicon.ico`           | Icon used for `.exe` packaging            |
| `README.md`             | Project overview                          |

---

## 🙌 Contributing

Pull requests, bug reports, and feature ideas are welcome!

Please fork the repo, make your changes in a branch, and submit a pull request with a clear description.

---

## ☕ Support Rupu

If you enjoy using this tool and want to support its development:

<a href="https://ko-fi.com/rupsiedaisy" target="_blank">
  <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Support me on Ko-fi">
</a>

Or visit: [https://ko-fi.com/rupsiedaisy](https://ko-fi.com/rupsiedaisy)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

- TTS engine powered by [Coqui TTS](https://github.com/coqui-ai/TTS)
- GUI and packaging by **Rupu**
# Rupu TTS

**Rupu TTS** is a lightweight, portable, and open-source text-to-speech (TTS) desktop application. Built with Python and Coqui TTS, it provides a user-friendly interface for generating high-quality speech from text — entirely offline.

...

## 🙏 Credits

- Text-to-Speech powered by [Coqui TTS](https://github.com/coqui-ai/TTS)
- GUI and packaging by **Rupu**
