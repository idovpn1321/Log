import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinter.scrolledtext as scrolledtext
from ttkbootstrap import Style
import logging
from datetime import datetime
import re
import pyperclip  # Untuk copy ke clipboard

# ====================== SETUP MATERIAL YOU THEME ======================
MATERIAL_YOU_THEME = {
    "primary": "#6750A4",
    "secondary": "#958DA5",
    "error": "#F2B8B5",
    "warning": "#FFD8B2",
    "success": "#B8E1B8",
    "background": "#1C1B1F",
    "surface": "#2D2B36",
    "text": "#E6E1E5",
}

class LogSeekerApp:
    def __init__(self, root):
        self.root = root
        self.setup_theme()
        self.setup_logging()
        self.setup_ui()
        self.scan_mode = "log"  # Default: 'log' or 'code'
        self.current_results = []
        
    def setup_theme(self):
        """Apply Material You theme colors"""
        self.style = Style(theme="darkly")
        self.style.configure("TFrame", background=MATERIAL_YOU_THEME["background"])
        self.style.configure("TLabel", background=MATERIAL_YOU_THEME["background"], foreground=MATERIAL_YOU_THEME["text"])
        self.style.configure("TButton", background=MATERIAL_YOU_THEME["primary"], foreground="white", font=('Roboto', 10))
        self.style.configure("TEntry", fieldbackground=MATERIAL_YOU_THEME["surface"], foreground=MATERIAL_YOU_THEME["text"])
        self.style.configure("TCombobox", fieldbackground=MATERIAL_YOU_THEME["surface"])
        self.style.configure("TScrollbar", background=MATERIAL_YOU_THEME["surface"])
        
    def setup_logging(self):
        """Configure logging"""
        logging.basicConfig(
            filename='zuanlogseeker_errors.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            encoding='utf-8'
        )
        logging.info("ZuanLogSeekr v4 started")

    def setup_ui(self):
        """Setup the modern UI"""
        self.root.title("ZuanLogSeekr v4")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        
        # Main container
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(
            header_frame,
            text="ZuanLogSeekr",
            font=('Roboto', 18, 'bold'),
            foreground=MATERIAL_YOU_THEME["primary"]
        ).pack(side=tk.LEFT, padx=10)
        
        # Controls
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=10)
        
        # File selection
        ttk.Label(control_frame, text="File:").grid(row=0, column=0, padx=5, sticky=tk.W)
        self.file_var = tk.StringVar()
        file_entry = ttk.Entry(control_frame, textvariable=self.file_var, width=60)
        file_entry.grid(row=0, column=1, padx=5, sticky=tk.W)
        
        browse_btn = ttk.Button(
            control_frame,
            text="📁 Browse",
            command=self.browse_file,
            style='primary.TButton'
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
        
        # Scan button
        scan_btn = ttk.Button(
            control_frame,
            text="🔍 Scan",
            command=self.scan_file,
            style='primary.TButton'
        )
        scan_btn.grid(row=0, column=5, padx=5)
        
        # Copy button
        self.copy_btn = ttk.Button(
            control_frame,
            text="📋 Copy",
            command=self.copy_errors,
            style='info.TButton',
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
            bg=MATERIAL_YOU_THEME["surface"],
            fg=MATERIAL_YOU_THEME["text"],
            insertbackground=MATERIAL_YOU_THEME["text"]
        )
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags for styling
        self.result_text.tag_config("header", foreground=MATERIAL_YOU_THEME["primary"], font=('Roboto', 12, 'bold'))
        self.result_text.tag_config("error", foreground=MATERIAL_YOU_THEME["error"])
        self.result_text.tag_config("warning", foreground=MATERIAL_YOU_THEME["warning"])
        self.result_text.tag_config("success", foreground=MATERIAL_YOU_THEME["success"])
        
        # Status bar
        self.status_var = tk.StringVar(value="🚀 Ready to scan")
        status_bar = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.FLAT,
            anchor=tk.W,
            font=('Roboto', 9),
            foreground=MATERIAL_YOU_THEME["secondary"]
        )
        status_bar.pack(fill=tk.X, pady=(5, 0))
    
    def browse_file(self):
        """Open file dialog"""
        filepath = filedialog.askopenfilename(
            title="Select File",
            filetypes=[("Logs", "*.log"), ("Code", "*.py"), ("Text", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            self.file_var.set(filepath)
            self.status_var.set(f"📂 Selected: {filepath}")
            # Auto-set mode based on file extension
            if filepath.endswith('.py'):
                self.mode_var.set('code')
            else:
                self.mode_var.set('log')
    
    def scan_file(self):
        """Scan the selected file"""
        filepath = self.file_var.get()
        if not filepath:
            messagebox.showwarning("⚠️ Missing File", "Please select a file first.")
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
        """Scan log lines for errors"""
        issues = []
        line_lower = line.lower()
        
        error_patterns = [
            r'\berror\b', r'\bfail(?:ed|ure)?\b', r'\bfatal\b',
            r'\bcrash\b', r'\bexception\b', r'\btimeout\b'
        ]
        
        warning_patterns = [
            r'\bwarn(?:ing)?\b', r'\bunable\b', r'\bcannot\b',
            r'\bdenied\b', r'\bnot found\b'
        ]
        
        for pattern in error_patterns:
            if re.search(pattern, line_lower):
                issues.append((line_num, line, "error"))
                break
        
        if not issues:
            for pattern in warning_patterns:
                if re.search(pattern, line_lower):
                    issues.append((line_num, line, "warning"))
                    break
        
        return issues
    
    def _scan_code_line(self, line, line_num):
        """Scan code lines for issues (without false positives)"""
        issues = []
        stripped_line = line.strip()
        if not stripped_line or stripped_line.startswith(('#', '"', "'")):
            return issues
        
        line_lower = stripped_line.lower()
        
        # Only detect real code issues, not variable declarations
        error_patterns = [
            r'except\s*:',  # Bare except
            r'print\s*\(',  # Leftover debug prints
            r'assert\s+True',  # Useless assert
            r'==\s*None'  # Should use 'is None'
        ]
        
        warning_patterns = [
            r'if\s+.*==\s*True',  # Redundant comparison
            r'while\s+True\s*:',  # Infinite loop
            r'len\s*\(.*\)\s*>\s*0'  # Should use truthiness check
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
        """Display results in a clean format"""
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
    
    def copy_errors(self):
        """Copy results to clipboard"""
        if not self.current_results:
            messagebox.showwarning("⚠️ No Results", "Nothing to copy.")
            return
        
        copy_text = "ZuanLogSeekr Results:\n\n"
        for line_num, line, issue_type in self.current_results:
            copy_text += f"[{issue_type.upper()}] Line {line_num}: {line}\n"
        
        pyperclip.copy(copy_text)
        self.status_var.set("📋 Copied to clipboard!")
    
    def _handle_error(self, error_msg):
        """Show error messages cleanly"""
        messagebox.showerror("Error", error_msg)
        self.status_var.set(error_msg)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, error_msg, "error")
        self.copy_btn['state'] = 'disabled'

if __name__ == "__main__":
    root = tk.Tk()
    app = LogSeekerApp(root)
    root.mainloop()
