import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import tempfile
import threading
import unicodedata
import sys

# Function to ensure correct pathing for resources (important for PyInstaller)
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Set startupinfo to suppress CMD windows on Windows
startupinfo = None
if sys.platform == "win32":
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

DEFAULT_VOICE = "tts_models/en/ljspeech/tacotron2-DDC"
OUTPUT_FORMATS = ["wav", "mp3", "flac"]
current_format = "wav"
theme_is_dark = True

# Dark and light themes
colors = {
    "dark": {
        "bg": "#1e1e1e", "fg": "#e0e0e0", "entry": "#2a2a2a", "highlight": "#3c3c3c",
        "button": "#333333", "active": "#444444", "selected": "#555555", "border": "#3c3c3c"
    },
    "light": {
        "bg": "#f4f4f4", "fg": "#1e1e1e", "entry": "#ffffff", "highlight": "#e0e0e0",
        "button": "#dddddd", "active": "#cccccc", "selected": "#bbbbbb", "border": "#c0c0c0"
    }
}

def clean_text(text):
    normalized = unicodedata.normalize("NFKD", text)
    return ''.join(c for c in normalized if not unicodedata.combining(c))

def run_tts():
    user_input = text_input.get("1.0", tk.END).strip()
    user_input = clean_text(user_input)
    file_base = filename_entry.get().strip()

    if not user_input:
        messagebox.showwarning("Input Missing", "Please enter some text.")
        return

    if not file_base:
        messagebox.showwarning("Filename Missing", "Please enter an output filename.")
        return

    file_base = os.path.splitext(file_base)[0]
    output_path = f"{file_base}.{current_format}"

    command = [
        "tts", "--text", user_input,
        "--model_name", DEFAULT_VOICE,
        "--out_path", output_path
    ]

    try:
        result = subprocess.run(command, capture_output=True, text=True, startupinfo=startupinfo)
        if result.returncode != 0:
            print("[ERROR] TTS command failed:")
            print(result.stderr or "Unknown error")
            messagebox.showerror("TTS Error", "TTS failed to generate output.\nCheck the terminal for details.")
            return

        if os.path.exists(output_path):
            messagebox.showinfo("Success", f"Speech saved to: {output_path}")
        else:
            messagebox.showerror("No Output", "TTS ran but no output file was created.")
    except Exception as e:
        print("[EXCEPTION] Error running TTS:", e)
        messagebox.showerror("Execution Error", f"An error occurred:\n{e}")

def set_output_format(fmt):
    global current_format
    current_format = fmt
    update_format_buttons()

def update_format_buttons():
    for fmt, btn in format_buttons.items():
        selected = fmt == current_format
        btn.config(
            bg=get("selected" if selected else "button"),
            fg=get("fg"),
            activebackground=get("active"),
            relief=tk.SUNKEN if selected else tk.RAISED
        )

def toggle_theme():
    global theme_is_dark
    theme_is_dark = not theme_is_dark
    apply_theme()

def get(key):
    return colors["dark" if theme_is_dark else "light"][key]

def apply_theme():
    window.config(bg=get("bg"))
    for widget in [text_input, filename_entry]:
        widget.config(bg=get("entry"), fg=get("fg"), insertbackground=get("fg"), highlightbackground=get("border"))
    for btn in [generate_button, theme_button]:
        btn.config(bg=get("button"), fg=get("fg"), activebackground=get("active"))
    for label in [label_input, label_filename, label_format]:
        label.config(bg=get("bg"), fg=get("fg"))
    update_format_buttons()

def focus_next(event):
    event.widget.tk_focusNext().focus()
    return "break"

def focus_prev(event):
    event.widget.tk_focusPrev().focus()
    return "break"

# --- GUI Setup ---
window = tk.Tk()
window.title("Rupu TTS")
window.geometry("560x520")
window.minsize(480, 460)

# Optional custom icon for EXE builds
try:
    window.iconbitmap(resource_path("appicon.ico"))
except Exception:
    pass  # fallback if icon is missing

# --- Text Input ---
label_input = tk.Label(window, text="Enter text to synthesize:", font=("Arial", 12))
label_input.pack(pady=(10, 3))
text_input = tk.Text(window, height=8, wrap="word", font=("Arial", 11), relief=tk.FLAT, bd=5)
text_input.pack(padx=10, fill="both", expand=True)
text_input.bind("<Tab>", focus_next)
text_input.bind("<Shift-Tab>", focus_prev)

# --- Filename Entry ---
label_filename = tk.Label(window, text="Output filename:", font=("Arial", 11))
label_filename.pack(pady=(10, 2))
filename_entry = tk.Entry(window, font=("Arial", 11), relief=tk.FLAT, bd=3)
filename_entry.pack(padx=10, fill="x")

# --- Output Format Buttons ---
label_format = tk.Label(window, text="Output format:", font=("Arial", 11))
label_format.pack(pady=(12, 2))

format_frame = tk.Frame(window)
format_frame.pack(pady=(0, 10))
format_buttons = {}
for fmt in OUTPUT_FORMATS:
    btn = tk.Button(format_frame, text=fmt.upper(), width=8, font=("Arial", 10),
                    command=lambda f=fmt: set_output_format(f))
    btn.pack(side="left", padx=5)
    format_buttons[fmt] = btn

# --- Action Buttons ---
generate_button = tk.Button(window, text="Generate Speech", command=run_tts, font=("Arial", 12), height=2)
generate_button.pack(pady=(5, 5), padx=10, fill="x")

theme_button = tk.Button(window, text="Toggle Light/Dark Mode", command=toggle_theme, font=("Arial", 10))
theme_button.pack(pady=(0, 10), padx=10, fill="x")

# --- Context Menus ---
def create_context_menu(widget):
    menu = tk.Menu(widget, tearoff=0)
    menu.add_command(label="Cut", command=lambda: widget.event_generate("<<Cut>>"))
    menu.add_command(label="Copy", command=lambda: widget.event_generate("<<Copy>>"))
    menu.add_command(label="Paste", command=lambda: widget.event_generate("<<Paste>>"))
    menu.add_separator()
    menu.add_command(label="Select All", command=lambda: widget.event_generate("<<SelectAll>>"))

    def show_menu(event):
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()

    widget.bind("<Button-3>", show_menu)
    return menu

# Bind context menus
create_context_menu(text_input)
create_context_menu(filename_entry)

# --- Final Theming ---
apply_theme()
window.mainloop()