#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import logging
import os
import re
from datetime import datetime

class LinuxLogSeeker:
    def __init__(self, root):
        self.root = root
        self.current_file = ""
        self.current_results = []
        
        # Initialize with light theme by default
        self.theme_mode = 'light'  
        self.themes = {
            'light': {
                'primary': '#1a5fb4',  # GNOME blue
                'surface': '#ffffff',
                'background': '#f6f5f4',
                'error': '#c01c28',
                'warning': '#e5a50a',
                'success': '#26a269',
                'text': '#241f31',
                'secondary': '#5e5c64'
            },
            'dark': {
                'primary': '#3584e4',  # GNOME blue
                'surface': '#242424',
                'background': '#1e1e1e',
                'error': '#ff7b63',
                'warning': '#ffbe6f',
                'success': '#8ff0a4',
                'text': '#ffffff',
                'secondary': '#deddda'
            }
        }
        
        self.setup_ui()
        self.setup_logging()

    def setup_logging(self):
        """Configure logging for Linux"""
        log_dir = os.path.expanduser("~/.local/share/zuanlogseeker")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        logging.basicConfig(
            filename=os.path.join(log_dir, 'app.log'),
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info("Application started")

    def setup_ui(self):
        """GNOME-inspired UI that works on XFCE"""
        self.root.title("ZuanLogSeekr for Linux")
        self.root.geometry("1000x700")
        
        # Main container
        main_frame = ttk.Frame(self.root, padding=12)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header bar
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 12))
        
        ttk.Label(
            header_frame,
            text="ZuanLogSeekr",
            font=('Sans 11 bold'),
            foreground=self.themes[self.theme_mode]['primary']
        ).pack(side=tk.LEFT)
        
        # Theme toggle button
        self.theme_btn = ttk.Button(
            header_frame,
            text="🌓",
            command=self.toggle_theme,
            width=3
        )
        self.theme_btn.pack(side=tk.RIGHT, padx=4)
        
        # Control panel
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=(0, 12))
        
        # File selection
        file_btn = ttk.Button(
            control_frame,
            text="Open File",
            command=self.browse_file
        )
        file_btn.pack(side=tk.LEFT, padx=4)
        
        self.file_label = ttk.Label(
            control_frame,
            text="No file selected",
            foreground=self.themes[self.theme_mode]['secondary']
        )
        self.file_label.pack(side=tk.LEFT, padx=8)
        
        # Analysis button
        analyze_btn = ttk.Button(
            control_frame,
            text="Analyze",
            command=self.analyze_file
        )
        analyze_btn.pack(side=tk.RIGHT, padx=4)
        
        # Results area
        self.result_text = scrolledtext.ScrolledText(
            main_frame,
            wrap=tk.WORD,
            font=('Monospace 10'),
            height=25,
            padx=12,
            pady=12,
            bg=self.themes[self.theme_mode]['surface'],
            fg=self.themes[self.theme_mode]['text'],
            insertbackground=self.themes[self.theme_mode]['text'],
            relief=tk.FLAT
        )
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags
        self.setup_text_tags()
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready to analyze files")
        status_bar = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.FLAT,
            anchor=tk.W,
            font=('Sans 9'),
            foreground=self.themes[self.theme_mode]['secondary']
        )
        status_bar.pack(fill=tk.X, pady=(6, 0))
        
        self.apply_theme()

    def setup_text_tags(self):
        """Configure text display styles"""
        tags_config = {
            'ERROR': {'foreground': self.themes[self.theme_mode]['error'], 'font': 'Monospace 10 bold'},
            'WARNING': {'foreground': self.themes[self.theme_mode]['warning'], 'font': 'Monospace 10 bold'},
            'INFO': {'foreground': self.themes[self.theme_mode]['primary'], 'font': 'Monospace 10'},
            'SUCCESS': {'foreground': self.themes[self.theme_mode]['success'], 'font': 'Monospace 10 bold'},
            'HEADER': {'foreground': self.themes[self.theme_mode]['primary'], 'font': 'Sans 12 bold'}
        }
        
        for tag, config in tags_config.items():
            self.result_text.tag_config(tag, **config)

    def apply_theme(self):
        """Apply the current theme colors"""
        theme = self.themes[self.theme_mode]
        
        # Configure styles
        style = ttk.Style()
        style.configure(
            '.',
            background=theme['background'],
            foreground=theme['text'],
            font=('Sans 10')
        )
        
        style.configure(
            'TButton',
            background=theme['primary'],
            foreground='white',
            padding=6,
            relief='flat'
        )
        
        # Update widget colors
        self.result_text.configure(
            bg=theme['surface'],
            fg=theme['text'],
            insertbackground=theme['text']
        )
        
        self.file_label.config(foreground=theme['secondary'])
        self.setup_text_tags()

    def toggle_theme(self):
        """Switch between light and dark themes"""
        self.theme_mode = 'dark' if self.theme_mode == 'light' else 'light'
        self.apply_theme()
        self.status_var.set(f"Switched to {self.theme_mode} mode")

    def browse_file(self):
        """Open file dialog"""
        filepath = filedialog.askopenfilename(
            title="Select File",
            filetypes=[
                ("Log Files", "*.log"),
                ("Python Files", "*.py"),
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )
        if filepath:
            self.current_file = filepath
            self.file_label.config(text=os.path.basename(filepath))
            self.status_var.set(f"Selected: {os.path.basename(filepath)}")

    def analyze_file(self):
        """Analyze the selected file"""
        if not self.current_file:
            messagebox.showwarning("No File", "Please select a file first")
            return
        
        try:
            self.current_results = []
            with open(self.current_file, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    stripped_line = line.strip()
                    if not stripped_line:
                        continue
                    
                    # Simple detection logic - customize as needed
                    line_lower = line.lower()
                    if 'error' in line_lower:
                        self.current_results.append(('ERROR', line_num, line))
                    elif 'warn' in line_lower:
                        self.current_results.append(('WARNING', line_num, line))
                    elif 'todo' in line_lower:
                        self.current_results.append(('INFO', line_num, line))
            
            self.display_results()
        
        except Exception as e:
            self.handle_error(f"Analysis error: {str(e)}")

    def display_results(self):
        """Display analysis results"""
        self.result_text.delete(1.0, tk.END)
        
        if not self.current_results:
            self.result_text.insert(tk.END, "✅ No issues found\n", "SUCCESS")
            self.status_var.set("Analysis complete - No issues found")
            return
        
        self.result_text.insert(tk.END, f"Analysis of: {os.path.basename(self.current_file)}\n\n", "HEADER")
        
        for level, line_num, line in self.current_results:
            self.result_text.insert(tk.END, f"[{level}] Line {line_num}:\n", level)
            self.result_text.insert(tk.END, f"{line}\n\n", level)
        
        self.status_var.set(f"Found {len(self.current_results)} issues")

    def handle_error(self, error_msg):
        """Error handling"""
        messagebox.showerror("Error", error_msg)
        self.status_var.set(error_msg)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, error_msg, "ERROR")

if __name__ == "__main__":
    root = tk.Tk()
    app = LinuxLogSeeker(root)
    root.mainloop()
