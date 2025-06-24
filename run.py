import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("Log files", "*.log *.txt"), ("All files", "*.*")])
    if filepath:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filepath)

def search_string():
    filepath = file_entry.get()
    search_term = keyword_entry.get()

    if not filepath or not search_term:
        messagebox.showwarning("Input Error", "Both log file and keyword must be provided.")
        return

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        messagebox.showerror("File Error", f"Could not open file:\n{str(e)}")
        return

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)

    for i, line in enumerate(lines, 1):
        if search_term.lower() in line.lower():
            result_text.insert(tk.END, f"[Line {i}]: {line}", "highlight")

    result_text.tag_config("highlight", foreground="red")
    result_text.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("ZuanLogSeekr")
root.geometry("700x500")
root.resizable(False, False)

# Input Frame
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.X)

tk.Label(frame, text="Log File:").grid(row=0, column=0, sticky="w")
file_entry = tk.Entry(frame, width=60)
file_entry.grid(row=0, column=1, padx=5)
browse_btn = tk.Button(frame, text="Browse", command=browse_file)
browse_btn.grid(row=0, column=2)

tk.Label(frame, text="Search Keyword:").grid(row=1, column=0, sticky="w")
keyword_entry = tk.Entry(frame, width=40)
keyword_entry.grid(row=1, column=1, padx=5, pady=10, sticky="w")
search_btn = tk.Button(frame, text="Search", command=search_string)
search_btn.grid(row=1, column=2)

# Result Text Box
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 10))
result_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
result_text.config(state=tk.DISABLED)

root.mainloop()
