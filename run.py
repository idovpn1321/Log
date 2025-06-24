import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinter.scrolledtext as scrolledtext
from ttkbootstrap import Style
import logging
from datetime import datetime
import re

class LogSeekerApp:
    def __init__(self, root):
        self.root = root
        self.style = Style(theme='darkly')
        self.setup_logging()
        self.setup_ui()
        self.scan_mode = "log"  # Default mode: 'log' or 'code'
        
    def setup_logging(self):
        """Configure logging for the application"""
        logging.basicConfig(
            filename='zuanlogseeker_errors.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            encoding='utf-8'
        )
        logging.info("Application started")

    def setup_ui(self):
        """Setup the main application UI"""
        self.root.title("ZuanLogSeekr v3 - Universal Error Detector")
        self.root.geometry("1000x700")
        
        # Configure styles
        self.style.configure('TButton', font=('Helvetica', 10))
        self.style.configure('TLabel', font=('Helvetica', 10))
        
        # Main container
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Top controls frame
        control_frame = ttk.LabelFrame(main_frame, text="Controls", padding=10)
        control_frame.pack(fill=tk.X, pady=5)
        
        # File selection
        ttk.Label(control_frame, text="File:").grid(row=0, column=0, sticky=tk.W)
        self.file_var = tk.StringVar()
        file_entry = ttk.Entry(control_frame, textvariable=self.file_var, width=60)
        file_entry.grid(row=0, column=1, padx=5, sticky=tk.W)
        
        browse_btn = ttk.Button(
            control_frame, 
            text="Browse", 
            command=self.browse_file,
            style='primary.TButton'
        )
        browse_btn.grid(row=0, column=2, padx=5)
        
        # Scan mode selection
        ttk.Label(control_frame, text="Scan Mode:").grid(row=0, column=3, padx=(20,5), sticky=tk.W)
        self.mode_var = tk.StringVar(value='log')
        mode_menu = ttk.OptionMenu(
            control_frame,
            self.mode_var,
            'log',
            'log',
            'code',
            command=self.change_mode
        )
        mode_menu.grid(row=0, column=4, sticky=tk.W)
        
        # Scan button
        scan_btn = ttk.Button(
            control_frame,
            text="Scan File",
            command=self.scan_file,
            style='danger.TButton'
        )
        scan_btn.grid(row=0, column=5, padx=5)
        
        # Theme selection
        ttk.Label(control_frame, text="Theme:").grid(row=1, column=0, sticky=tk.W, pady=(10,0))
        self.theme_var = tk.StringVar(value='darkly')
        theme_menu = ttk.OptionMenu(
            control_frame,
            self.theme_var,
            'darkly',
            *self.style.theme_names(),
            command=self.change_theme
        )
        theme_menu.grid(row=1, column=1, sticky=tk.W, pady=(10,0))
        
        # Results display
        results_frame = ttk.LabelFrame(main_frame, text="Scan Results", padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.result_text = scrolledtext.ScrolledText(
            results_frame,
            wrap=tk.WORD,
            font=('Consolas', 10),
            height=25,
            padx=10,
            pady=10
        )
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags for styling
        self.result_text.tag_config("header", foreground="#4fc3f7", font=('Consolas', 11, 'bold'))
        self.result_text.tag_config("line_num", foreground="#ff7043")
        self.result_text.tag_config("error", foreground="#ff5252", background="#1e1e1e")
        self.result_text.tag_config("warning", foreground="#ffd740", background="#1e1e1e")
        self.result_text.tag_config("info", foreground="#69f0ae", background="#1e1e1e")
        self.result_text.tag_config("summary", foreground="#69f0ae", font=('Consolas', 10, 'bold'))
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready to scan. Select a file and click 'Scan File'")
        status_bar = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            font=('Helvetica', 9)
        )
        status_bar.pack(fill=tk.X, pady=(5,0))
    
    def browse_file(self):
        """Open file dialog to select file"""
        file_types = [
            ("Log files", "*.log"),
            ("Text files", "*.txt"), 
            ("Python files", "*.py"),
            ("All files", "*.*")
        ]
        
        filepath = filedialog.askopenfilename(
            title="Select File to Scan",
            filetypes=file_types
        )
        
        if filepath:
            self.file_var.set(filepath)
            self.status_var.set(f"Selected: {filepath}")
            logging.info(f"Selected file: {filepath}")
            
            # Auto-detect scan mode based on file extension
            if filepath.endswith('.py'):
                self.mode_var.set('code')
            else:
                self.mode_var.set('log')
    
    def change_mode(self, mode):
        """Change scan mode between log and code"""
        self.scan_mode = mode
        self.status_var.set(f"Scan mode set to: {mode} mode")
        logging.info(f"Scan mode changed to {mode}")
    
    def scan_file(self):
        """Scan the selected file for errors"""
        filepath = self.file_var.get()
        if not filepath:
            messagebox.showwarning("Missing File", "Please select a valid file first.")
            logging.warning("Scan attempted without file selection")
            return

        try:
            found_lines = []
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    try:
                        stripped_line = line.strip()
                        
                        # Skip empty lines
                        if not stripped_line:
                            continue
                            
                        # Different processing for log vs code files
                        if self.scan_mode == 'log':
                            issues = self._scan_log_line(stripped_line)
                        else:
                            issues = self._scan_code_line(stripped_line, line_num)
                            
                        if issues:
                            found_lines.extend(issues)
                            
                    except UnicodeDecodeError as ude:
                        logging.error(f"Unicode decode error in line {line_num}: {ude}")
                        continue
                    except Exception as e:
                        logging.error(f"Error processing line {line_num}: {e}")
                        continue

            self._display_results(found_lines, filepath)

        except FileNotFoundError:
            self._handle_error(f"File not found: {filepath}", "Error: File not found")
        except PermissionError:
            self._handle_error(f"Permission denied when accessing: {filepath}", "Error: Permission denied")
        except Exception as e:
            self._handle_error(f"Unexpected error: {str(e)}", "Error: Processing failed")
    
    def _scan_log_line(self, line):
        """Scan a single log line for issues"""
        issues = []
        line_lower = line.lower()
        
        # Error patterns
        error_patterns = [
            r'\berror\b', r'\bfail(?:ed|ure)?\b', r'\bfatal\b',
            r'\bcrash\b', r'\bpanic\b', r'\babort\b',
            r'\bsegfault\b', r'\bexception\b'
        ]
        
        # Warning patterns
        warning_patterns = [
            r'\bwarn(?:ing)?\b', r'\bunable\b', r'\bcannot\b',
            r'\btimeout\b', r'\bmissing\b', r'\bdenied\b',
            r'\bnot found\b', r'\bno such\b'
        ]
        
        # Check for error patterns
        for pattern in error_patterns:
            if re.search(pattern, line_lower):
                issues.append((line_num, line, "error"))
                break
                
        # Check for warning patterns if no error found
        if not issues:
            for pattern in warning_patterns:
                if re.search(pattern, line_lower):
                    issues.append((line_num, line, "warning"))
                    break
        
        return issues
    
    def _scan_code_line(self, line, line_num):
        """Scan a single code line for issues"""
        issues = []
        line_lower = line.lower()
        
        # Skip comments and docstrings
        if line_lower.startswith('#') or line_lower.startswith('"""') or line_lower.startswith("'''"):
            return issues
            
        # Check for common code issues
        if any(kw in line_lower for kw in ["except:", "except exception", "print("]):
            issues.append((line_num, line, "warning"))
        
        return issues
    
    def _display_results(self, found_lines, filepath):
        """Display the scan results"""
        self.result_text.delete(1.0, tk.END)
        
        if found_lines:
            # Group by error type
            errors = [x for x in found_lines if x[2] == "error"]
            warnings = [x for x in found_lines if x[2] == "warning"]
            
            # Display summary
            self.result_text.insert(tk.END, 
                f"Scan Results for: {filepath}\n\n"
                f"• Errors found: {len(errors)}\n"
                f"• Warnings found: {len(warnings)}\n\n",
                "header")
            
            # Display errors
            if errors:
                self.result_text.insert(tk.END, "=== ERRORS ===\n", "header")
                for line_num, line, _ in errors:
                    self.result_text.insert(tk.END, f"Line {line_num}: ", "line_num")
                    self.result_text.insert(tk.END, f"{line}\n\n", "error")
            
            # Display warnings
            if warnings:
                self.result_text.insert(tk.END, "=== WARNINGS ===\n", "header")
                for line_num, line, _ in warnings:
                    self.result_text.insert(tk.END, f"Line {line_num}: ", "line_num")
                    self.result_text.insert(tk.END, f"{line}\n\n", "warning")
            
            self.status_var.set(f"Scan complete. Found {len(found_lines)} issues ({len(errors)} errors, {len(warnings)} warnings).")
            logging.info(f"Scan completed with {len(found_lines)} issues found in {filepath}")
        else:
            self.result_text.insert(tk.END, 
                f"No issues found in: {filepath}\n\n"
                "The file appears to be clean based on current scan criteria.",
                "header")
            self.status_var.set("Scan complete. No issues found.")
            logging.info(f"Scan completed - no issues found in {filepath}")
    
    def _handle_error(self, error_msg, status_msg):
        """Handle and display errors"""
        messagebox.showerror("File Error", error_msg)
        logging.error(error_msg, exc_info=True)
        self.status_var.set(status_msg)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, error_msg, "error")
    
    def change_theme(self, theme):
        """Change the application theme"""
        try:
            self.style.theme_use(theme)
            logging.info(f"Theme changed to {theme}")
            self.status_var.set(f"Theme changed to {theme}")
        except Exception as e:
            logging.error(f"Theme switch error: {e}", exc_info=True)
            self.status_var.set("Theme change failed")

if __name__ == "__main__":
    root = tk.Tk()
    app = LogSeekerApp(root)
    root.mainloop()
