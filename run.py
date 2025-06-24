import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog
import os
from tkinter import messagebox

# ====================== ERROR DETECTION KEYWORDS ======================
ERROR_KEYWORDS = [
    "fail", "error", "unable", "not found", "exception",
    "cannot", "no such", "permission denied", "timeout",
    "segfault", "panic", "missing", "denied", "abort",
    "fatal", "unreachable", "not registered", "unresolved"
]

# ====================== FUNCTIONALITY ======================
def browse_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        file_entry.delete(0, ttk.END)
        file_entry.insert(0, filepath)
        status_var.set(f"Opened: {os.path.basename(filepath)}")

def clear_result():
    result_text.config(state=ttk.NORMAL)
    result_text.delete("1.0", ttk.END)
    result_text.config(state=ttk.DISABLED)
    status_var.set("Result cleared.")

def scan_log():
    filepath = file_entry.get()

    if not os.path.isfile(filepath):
        ttk.dialogs.Messagebox.show_warning("Missing File", "Please select a valid log file.")
        return

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        ttk.dialogs.Messagebox.show_error("File Error", str(e))
        return

    result_text.config(state=ttk.NORMAL)
    result_text.delete("1.0", ttk.END)

    found_lines = []
    for i, line in enumerate(lines, 1):
        if any(err_kw in line.lower() for err_kw in ERROR_KEYWORDS):
            found_lines.append(f"[Line {i}] {line}")

    if found_lines:
        for line in found_lines:
            result_text.insert(ttk.END, line, "highlight")
        result_text.insert(ttk.END, f"\nTotal errors found: {len(found_lines)}", "summary")
        status_var.set(f"Scan complete. {len(found_lines)} error lines found.")
    else:
        result_text.insert(ttk.END, "No error-related patterns found.")
        status_var.set("Scan complete. No errors found.")

    result_text.tag_config("highlight", foreground="red")
    result_text.tag_config("summary", foreground="blue", font=("JetBrains Mono", 9, "bold"))
    result_text.config(state=ttk.DISABLED)

def toggle_theme():
    new_theme = "darkly" if style.theme.name == "flatly" else "flatly"
    style.theme_use(new_theme)
    status_var.set(f"Theme switched to {new_theme} mode.")

# ====================== GUI SETUP ======================
style = ttk.Style("flatly")
app = ttk.Window(themename="flatly")
app.title("ZuanLogSeekr v3 - Universal Error Detector")
app.geometry("850x600")
app.resizable(False, False)

# ==== TOP FRAME ====
top_frame = ttk.Frame(app, padding=10)
top_frame.pack(fill=ttk.X)

file_label = ttk.Label(top_frame, text="Log File:")
file_label.grid(row=0, column=0, sticky="w")

file_entry = ttk.Entry(top_frame, width=70)
file_entry.grid(row=0, column=1, padx=5)

browse_btn = ttk.Button(top_frame, text="Browse", command=browse_file, bootstyle="primary-outline")
browse_btn.grid(row=0, column=2)

scan_btn = ttk.Button(top_frame, text="Scan Errors", command=scan_log, bootstyle="danger")
scan_btn.grid(row=1, column=1, pady=10, sticky="w")

clear_btn = ttk.Button(top_frame, text="Clear Result", command=clear_result, bootstyle="secondary")
clear_btn.grid(row=1, column=0, pady=10, sticky="w")

theme_btn = ttk.Button(top_frame, text="🌙/☀️ Toggle Theme", command=toggle_theme, bootstyle="secondary")
theme_btn.grid(row=1, column=2, padx=5)

# ==== RESULT TEXT ====
result_text = ttk.ScrolledText(app, wrap="word", font=("JetBrains Mono", 10))
result_text.pack(fill="both", expand=True, padx=10, pady=(0, 0))
result_text.config(state=ttk.DISABLED)

# ==== STATUS BAR ====
status_var = ttk.StringVar(value="Ready.")
status_bar = ttk.Label(app, textvariable=status_var, anchor="w", padding=5, bootstyle="secondary")
status_bar.pack(fill=ttk.X, side=ttk.BOTTOM)

# ====================== PATCH THEME SWITCH ======================
original_theme_use = style.theme_use

def safe_theme_use(new_theme):
    try:
        if app.winfo_exists():
            original_theme_use(new_theme)
    except Exception as e:
        print("[!] Theme switch error (suppressed):", e)

style.theme_use = safe_theme_use

# ====================== CLEAN EXIT ======================
def on_close():
    theme_btn.config(state=ttk.DISABLED)
    scan_btn.config(state=ttk.DISABLED)
    browse_btn.config(state=ttk.DISABLED)
    clear_btn.config(state=ttk.DISABLED)
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_close)

# ====================== MAINLOOP ======================
app.mainloop()
