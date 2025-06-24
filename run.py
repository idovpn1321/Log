import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog
import os

def browse_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filepath)

def search_string():
    filepath = file_entry.get()
    search_term = keyword_entry.get()

    if not os.path.isfile(filepath) or not search_term.strip():
        ttk.dialogs.Messagebox.show_warning("Missing Input", "Please select a file and enter a keyword.")
        return

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        ttk.dialogs.Messagebox.show_error("File Error", f"Could not read file:\n{str(e)}")
        return

    result_text.config(state="normal")
    result_text.delete("1.0", "end")

    found = False
    for i, line in enumerate(lines, 1):
        if search_term.lower() in line.lower():
            result_text.insert("end", f"[Line {i}]  {line}", "highlight")
            found = True

    if not found:
        result_text.insert("end", "No matching lines found.")

    result_text.tag_config("highlight", foreground="red")
    result_text.config(state="disabled")

# ===== GUI START =====
app = ttk.Window(themename="minty")  # Coba juga: 'cyborg', 'superhero', 'morph', 'darkly'
app.title("ZuanLogSeekr - Material Inspired")
app.geometry("750x550")

# ==== Top Frame ====
frame = ttk.Frame(app, padding=10)
frame.pack(fill=X)

ttk.Label(frame, text="Log File:").grid(row=0, column=0, sticky="w")
file_entry = ttk.Entry(frame, width=60)
file_entry.grid(row=0, column=1, padx=5)
ttk.Button(frame, text="Browse", command=browse_file, bootstyle="primary-outline").grid(row=0, column=2)

ttk.Label(frame, text="Keyword:").grid(row=1, column=0, sticky="w", pady=10)
keyword_entry = ttk.Entry(frame, width=40)
keyword_entry.grid(row=1, column=1, padx=5, pady=10, sticky="w")
ttk.Button(frame, text="Search", command=search_string, bootstyle="success").grid(row=1, column=2)

# ==== Result Box ====
result_text = ttk.ScrolledText(app, wrap="word", font=("JetBrains Mono", 10))
result_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))
result_text.config(state="disabled")

app.mainloop()
