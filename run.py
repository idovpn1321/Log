import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinter.scrolledtext as scrolledtext
from ttkbootstrap import Style
import logging
from datetime import datetime
import re

# ====================== MATERIAL YOU THEME COLORS ======================
MATERIAL_YOU = {
    "primary": "#6750A4",
    "surface": "#2D2B36",
    "background": "#1C1B1F",
    "error": "#F2B8B5",
    "warning": "#FFD8B2",
    "success": "#B8E1B8",
    "text": "#E6E1E5",
    "secondary": "#958DA5"
}

class LogSeekerApp:
    def __init__(self, root):
        self.root = root
        self.setup_theme()
        self.setup_logging()
        self.setup_ui()
        self.scan_mode = "log"
        self.current_results = []
        
    def setup_theme(self):
        """Configure Material You theme"""
        self.style = Style(theme="darkly")
        self.style.configure(".", font=('Roboto', 10))
        
        # Apply colors
        self.root.configure(bg=MATERIAL_YOU["background"])
        self.style.configure(
            "TFrame", 
            background=MATERIAL_YOU["background"],
            relief="flat"
        )
        self.style.configure(
            "TLabel", 
            background=MATERIAL_YOU["background"],
            foreground=MATERIAL_YOU["text"]
        )
        self.style.configure(
            "TButton", 
            background=MATERIAL_YOU["primary"],
            foreground="white",
            bordercolor=MATERIAL_YOU["primary"],
            focuscolor=MATERIAL_YOU["primary"] + "30"  # Add transparency
        )
        self.style.map(
            "TButton",
            background=[("active", MATERIAL_YOU["primary"] + "DD")],
            bordercolor=[("active", MATERIAL_YOU["primary"] + "DD")]
        )

    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            filename='zuanlogseeker.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            encoding='utf-8'
        )
        logging.info("Application started")

    def setup_ui(self):
        """Setup user interface"""
        self.root.title("ZuanLogSeekr v4")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        
        # Main container
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(
            header_frame,
            text="ZuanLogSeekr",
            font=('Roboto', 18, 'bold'),
            foreground=MATERIAL_YOU["primary"]
        ).pack(side=tk.LEFT, padx=10)
        
        # Control panel
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=10)
        
        # File selection
        ttk.Label(control_frame, text="File:").grid(row=0, column=0, padx=5, sticky=tk.W)
        self.file_var = tk.StringVar()
        file_entry = ttk.Entry(
            control_frame, 
            textvariable=self.file_var, 
            width=60,
            style='TEntry'
        )
        file_entry.grid(row=0, column=1, padx=5, sticky=tk.W)
        
        browse_btn = ttk.Button(
            control_frame,
            text="📁 Browse",
            command=self.browse_file,
            style='TButton'
        )
        browse_btn.grid(row=0, column=2, padx=5)
        
        # Scan mode
        ttk.Label(control_frame, text="Mode:").grid(row=0, column=3, padx=5, sticky=tk.W)
        self.mode_var = tk.StringVar(value='log')
        mode_menu = ttk.Combobox(
            control_frame,
            textvariable=self.mode_var,
            values=['log', 'code'],
            state='readonly',
            width=8
        )
        mode_menu.grid(row=0, column=4, padx=5)
        
        # Action buttons
        scan_btn = ttk.Button(
            control_frame,
            text="🔍 Scan",
            command=self.scan_file,
            style='TButton'
        )
        scan_btn.grid(row=0, column=5, padx=5)
        
        self.copy_btn = ttk.Button(
            control_frame,
            text="📋 Copy",
            command=self.copy_to_clipboard,
            style='TButton',
            state='disabled'
        )
        self.copy_btn.grid(row=0, column=6, padx=5)
        
        # Results area
        results_frame = ttk.Frame(main_frame)
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        self.result_text = scrolledtext.ScrolledText(
            results_frame,
            wrap=tk.WORD,
            font=('Roboto', 10),
            height=25,
            padx=10,
            pady=10,
            bg=MATERIAL_YOU["surface"],
            fg=MATERIAL_YOU["text"],
            insertbackground=MATERIAL_YOU["text"],
            selectbackground=MATERIAL_YOU["primary"] + "60"
        )
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags
        self.result_text.tag_config("header", foreground=MATERIAL_YOU["primary"], font=('Roboto', 12, 'bold'))
        self.result_text.tag_config("error", foreground=MATERIAL_YOU["error"])
        self.result_text.tag_config("warning", foreground=MATERIAL_YOU["warning"])
        self.result_text.tag_config("success", foreground=MATERIAL_YOU["success"])
        
        # Status bar
        self.status_var = tk.StringVar(value="🚀 Ready to scan")
        status_bar = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.FLAT,
            anchor=tk.W,
            font=('Roboto', 9),
            foreground=MATERIAL_YOU["secondary"]
        )
        status_bar.pack(fill=tk.X, pady=(5, 0))
    
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
            self.file_var.set(filepath)
            self.status_var.set(f"📂 Selected: {filepath}")
            if filepath.endswith('.py'):
                self.mode_var.set('code')
            else:
                self.mode_var.set('log')
    
    def scan_file(self):
        """Scan the selected file"""
        filepath = self.file_var.get()
        if not filepath:
            messagebox.showwarning("Missing File", "Please select a file first.")
            return
        
        try:
            found_lines = []
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    stripped_line = line.strip()
                    if not stripped_line:
                        continue
                    
                    if self.mode_var.get() == 'log':
                        issues = self._scan_log_line(stripped_line, line_num)
                    else:
                        issues = self._scan_code_line(stripped_line, line_num)
                    
                    if issues:
                        found_lines.extend(issues)
            
            self.current_results = found_lines
            self._display_results(found_lines, filepath)
            self.copy_btn['state'] = 'normal' if found_lines else 'disabled'
        
        except Exception as e:
            self._handle_error(f"❌ Error: {str(e)}")
    
    def _scan_log_line(self, line, line_num):
        """Scan log file lines"""
        issues = []
        line_lower = line.lower()
        
        error_kws = ["error", "fail", "fatal", "crash", "exception", "timeout"]
        warning_kws = ["warn", "unable", "cannot", "denied", "not found"]
        
        if any(kw in line_lower for kw in error_kws):
            issues.append((line_num, line, "error"))
        elif any(kw in line_lower for kw in warning_kws):
            issues.append((line_num, line, "warning"))
        
        return issues
    
    def _scan_code_line(self, line, line_num):
        """Scan source code lines"""
        issues = []
        stripped_line = line.strip()
        
        # Skip comments and empty lines
        if not stripped_line or stripped_line.startswith(('#', '"', "'")):
            return issues
            
        line_lower = stripped_line.lower()
        
        # Error patterns
        error_patterns = [
            r'except\s*:',  # Bare except
            r'print\s*\(',  # Debug prints
            r'==\s*None',   # Should use 'is None'
            r'\bpass\b'     # Empty blocks
        ]
        
        # Warning patterns
        warning_patterns = [
            r'if\s+.*==\s*True',  # Redundant comparison
            r'while\s+True\s*:',   # Infinite loop
            r'len\s*\(.*\)\s*>\s*0'  # Truthiness check
        ]
        
        for pattern in error_patterns:
            if re.search(pattern, line_lower):
                issues.append((line_num, stripped_line, "error"))
                break
                
        if not issues:
            for pattern in warning_patterns:
                if re.search(pattern, line_lower):
                    issues.append((line_num, stripped_line, "warning"))
                    break
                    
        return issues
    
    def _display_results(self, found_lines, filepath):
        """Display scan results"""
        self.result_text.delete(1.0, tk.END)
        
        if not found_lines:
            self.result_text.insert(tk.END, f"✅ No issues found in:\n{filepath}\n", "success")
            self.status_var.set("✅ Scan complete - No issues found")
            return
            
        errors = [x for x in found_lines if x[2] == "error"]
        warnings = [x for x in found_lines if x[2] == "warning"]
        
        self.result_text.insert(tk.END, f"🔍 Scan Results for:\n{filepath}\n\n", "header")
        
        if errors:
            self.result_text.insert(tk.END, "🚨 Errors:\n", "header")
            for line_num, line, _ in errors:
                self.result_text.insert(tk.END, f"  L{line_num}: ", "header")
                self.result_text.insert(tk.END, f"{line}\n", "error")
        
        if warnings:
            self.result_text.insert(tk.END, "\n⚠️ Warnings:\n", "header")
            for line_num, line, _ in warnings:
                self.result_text.insert(tk.END, f"  L{line_num}: ", "header")
                self.result_text.insert(tk.END, f"{line}\n", "warning")
        
        self.status_var.set(f"📊 Found {len(errors)} errors, {len(warnings)} warnings")
    
    def copy_to_clipboard(self):
        """Copy results to clipboard without pyperclip"""
        if not self.current_results:
            messagebox.showwarning("No Results", "Nothing to copy.")
            return
            
        copy_text = "ZuanLogSeekr Results:\n\n"
        for line_num, line, issue_type in self.current_results:
            copy_text += f"[{issue_type.upper()}] Line {line_num}: {line}\n"
        
        # Copy to clipboard using tkinter
        self.root.clipboard_clear()
        self.root.clipboard_append(copy_text)
        self.root.update()  # Required to finalize the clipboard
        
        self.status_var.set("📋 Copied to clipboard!")
        messagebox.showinfo("Copied", "Results copied to clipboard!")
    
    def _handle_error(self, error_msg):
        """Handle and display errors"""
        messagebox.showerror("Error", error_msg)
        self.status_var.set(error_msg)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, error_msg, "error")
        self.copy_btn['state'] = 'disabled'

if __name__ == "__main__":
    root = tk.Tk()
    app = LogSeekerApp(root)
    root.mainloop()
