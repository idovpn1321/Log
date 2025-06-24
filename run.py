import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog
import os

# ====================== PREDEFINED PATTERNS ======================
ERROR_PATTERNS = [
    "could not ctl.interface.start",
    "not registered hwservice",
    "could not get transport for IMTs/default"
]

# ====================== FUNCTIONAL LOGIC ======================
def browse_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        file_entry.delete(0, ttk.END)
        file_entry.insert(0, filepath)

def scan_errors():
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

    found_any = False
    for i, line in enumerate(lines, 1):
        for pattern in ERROR_PATTERNS:
            if pattern in line:
                result_text.insert(ttk.END, f"[Line {i}] {line}", "highlight")
                found_any = True
                break

    if not found_any:
        result_text.insert(ttk.END, "No known error patterns found.")

    result_text.tag_config("highlight", foreground="red")
    result_text.config(state=ttk.DISABLED)

def toggle_theme():
    new_theme = "darkly" if style.theme.name == "flatly" else "flatly"
    style.theme_use(new_theme)

# ====================== GUI SETUP ======================
style = ttk.Style("flatly")  # default light theme
app = ttk.Window(themename="flatly")
app.title("ZuanLogSeekr v2")
app.geometry("800x580")
app.resizable(False, False)

# ==== TOP FRAME ====
frame = ttk.Frame(app, padding=10)
frame.pack(fill=ttk.X)

ttk.Label(frame, text="Log File:").grid(row=0, column=0, sticky="w")
file_entry = ttk.Entry(frame, width=60)
file_entry.grid(row=0, column=1, padx=5)
ttk.Button(frame, text="Browse", command=browse_file, bootstyle="primary-outline").grid(row=0, column=2)

ttk.Button(frame, text="Scan Errors", command=scan_errors, bootstyle="danger").grid(row=1, column=1, pady=10, sticky="w")

theme_toggle = ttk.Button(frame, text="🌓 Switch Theme", command=toggle_theme, bootstyle="secondary")
theme_toggle.grid(row=1, column=2, padx=5)

# ==== RESULT BOX ====
result_text = ttk.ScrolledText(app, wrap="word", font=("JetBrains Mono", 10))
result_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))
result_text.config(state=ttk.DISABLED)

# ====================== RUN ======================
app.mainloop()
