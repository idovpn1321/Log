#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os

class LinuxLogSeeker:
    def __init__(self, root):
        self.root = root
        self.current_file = ""
        self.current_results = []
        
        # Theme setup
        self.theme_mode = 'light'
        self.themes = {
            'light': {
                'primary': '#1a5fb4',
                'surface': '#ffffff',
                'text': '#000000'
            },
            'dark': {
                'primary': '#3584e4', 
                'surface': '#242424',
                'text': '#ffffff'
            }
        }
        
        self.setup_ui()

    def setup_ui(self):
        """Setup UI dengan fitur copy-paste"""
        self.root.title("ZuanLogSeekr XFCE")
        self.root.geometry("1000x700")
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Control panel
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=5)
        
        # Tombol-tombol
        ttk.Button(
            control_frame,
            text="Open File",
            command=self.browse_file
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            control_frame,
            text="Analyze",
            command=self.analyze_file
        ).pack(side=tk.LEFT, padx=5)
        
        # Tombol COPY baru!
        ttk.Button(
            control_frame,
            text="Copy Results",
            command=self.copy_results,
            style='primary.TButton'
        ).pack(side=tk.RIGHT, padx=5)
        
        # Hasil analisis
        self.result_text = scrolledtext.ScrolledText(
            main_frame,
            wrap=tk.WORD,
            font=('Monospace', 10),
            height=25,
            padx=10,
            pady=10
        )
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        ).pack(fill=tk.X, pady=(5,0))
        
        # Tag untuk styling
        self.result_text.tag_config('ERROR', foreground='red')
        self.result_text.tag_config('WARNING', foreground='orange')

    def browse_file(self):
        """Buka file dialog"""
        filepath = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if filepath:
            self.current_file = filepath
            self.status_var.set(f"File: {os.path.basename(filepath)}")

    def analyze_file(self):
        """Analisis file"""
        if not self.current_file:
            messagebox.showwarning("Error", "Pilih file dulu bro!")
            return
            
        try:
            self.current_results = []
            with open(self.current_file, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    if 'error' in line.lower():
                        self.current_results.append(f"ERROR Line {line_num}: {line}")
                    elif 'warn' in line.lower():
                        self.current_results.append(f"WARNING Line {line_num}: {line}")
            
            self.display_results()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal baca file: {str(e)}")

    def display_results(self):
        """Tampilkan hasil"""
        self.result_text.delete(1.0, tk.END)
        
        if not self.current_results:
            self.result_text.insert(tk.END, "Ga ada error bro, aman!")
            return
            
        for result in self.current_results:
            if 'ERROR' in result:
                self.result_text.insert(tk.END, result + '\n\n', 'ERROR')
            else:
                self.result_text.insert(tk.END, result + '\n\n', 'WARNING')
        
        self.status_var.set(f"Found {len(self.current_results)} issues")

    def copy_results(self):
        """Fitur COPY baru!"""
        if not self.current_results:
            messagebox.showwarning("Woi", "Ga ada hasil yang bisa dicopy!")
            return
            
        # Gabungin semua hasil
        text_to_copy = "\n".join(self.current_results)
        
        # Clear clipboard dan copy
        self.root.clipboard_clear()
        self.root.clipboard_append(text_to_copy)
        
        # Kasih notif
        messagebox.showinfo("Copied!", "Hasil udah dicopy ke clipboard!")
        self.status_var.set("Results copied to clipboard")

if __name__ == "__main__":
    root = tk.Tk()
    app = LinuxLogSeeker(root)
    root.mainloop()
