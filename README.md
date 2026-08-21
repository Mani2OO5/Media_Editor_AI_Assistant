# 🎬 FFmpeg Prompt Editor

⚠️ Project Status: Under Development / Not Stable
This project currently contains known bugs and may not work correctly. It is under active development.

A simple program that lets you edit your videos and audios (or literally any file you can edit with **FFmpeg**) just by typing a prompt. 🪄

It uses **Ollama** together with the **llama3.2** language model to understand your prompt, turn it into an FFmpeg configuration, and then automatically executes it — and your file gets edited. ✂️

> ⚠️ **Note:** `llama3.2` is a small and fast model, and it already works well enough with FFmpeg — but if you want even better results, feel free to use a stronger model instead. 🚀

---

## ✨ Features

- 🗣️ Edit media files using natural language prompts
- ⚙️ Automatically generates and runs the correct FFmpeg command
- 🔄 Works with any file format supported by FFmpeg (video, audio, etc.)
- 🧠 Powered by a local LLM via Ollama — no cloud API needed

---

## 📋 Requirements

- 🐍 Python **3.14.4**
- 🤖 [Ollama](https://ollama.com)
- 🎞️ [FFmpeg](https://ffmpeg.org)

---

## 🛠️ Installation

### 1️⃣ Install Ollama

**🐧 Linux**
```bash
sudo apt install ollama
```

**🍎 macOS**

You can install Ollama on macOS using any of the following methods:

- Download the app directly:
  👉 https://ollama.com/download/mac

- Or install via **Homebrew**:
```bash
brew install ollama
```

**🪟 Windows**

You can install Ollama on Windows using any of the following methods:

- Download the installer directly:
  👉 https://ollama.com/download/windows
  Then make sure it's added to your system `PATH`.

- Or install via **winget**:
```powershell
winget install Ollama.Ollama
```

✅ Once installed, pull the language model used by this program:
```bash
ollama pull llama3.2
```

> 💡 You can replace `llama3.2` with any other model supported by Ollama if you want better results — just make sure to update the model name in the program's configuration too.

---

### 2️⃣ Install FFmpeg

**🐧 Linux**
```bash
sudo apt install ffmpeg
```

**🍎 macOS**
```bash
brew install ffmpeg
```

**🪟 Windows**

You can install FFmpeg on Windows using any of the following methods:

- Download a prebuilt binary from the official builds page:
  👉 https://www.gyan.dev/ffmpeg/builds/
  Then extract it and add the `bin` folder to your system `PATH`.

- Or install via **winget**:
```powershell
winget install ffmpeg
```

- Or install via **Chocolatey**:
```powershell
choco install ffmpeg
```

---

### 3️⃣ Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Once everything is installed, simply run the program and describe the edit you want in plain language. The prompt will be processed by `llama3.2`, converted into an FFmpeg command, and executed automatically on your file. 🎉

---

## 👨🏻‍💻 Author

Created by Mani Arab

If you find this project useful, feel free to ⭐ the repo or fork it!
---

## ⚖️ License

This project is released under the MIT License, so you can freely use, modify, and share it.