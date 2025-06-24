import tkinter as tk
from tkinter import ttk, filedialog
import tkinter.scrolledtext as scrolledtext
from ttkbootstrap import Style
import logging
from datetime import datetime

# ====================== ERROR DETECTION KEYWORDS ======================
ERROR_KEYWORDS = [
    "fail", "error", "unable", "not found", "exception",
    "cannot", "no such", "permission denied", "timeout",
    "segfault", "panic", "missing", "denied", "abort",
    "fatal", "unreachable", "not registered", "unresolved",
    "crash", "corrupt", "invalid", "failed", "warning"
]

class LogSeekerApp:
    def __init__(self, root):
        self.root = root
        self.style = Style(theme='darkly')  # Create Style instance first
        self.setup_ui()
        self.setup_logging()
        
    def setup_logging(self):
        """Configure logging for the application"""
        logging.basicConfig(
            filename='zuanlogseeker_errors.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info("Application started")

    def setup_ui(self):
        """Setup the main application UI"""
        self.root.title("ZuanLogSeekr v3 - Universal Error Detector")
        self.root.geometry("900x650")
        
        # Main container
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Top controls frame
        control_frame = ttk.LabelFrame(main_frame, text="Controls", padding=10)
        control_frame.pack(fill=tk.X, pady=5)
        
        # File selection
        ttk.Label(control_frame, text="Log File:").grid(row=0, column=0, sticky=tk.W)
        self.file_var = tk.StringVar()
        file_entry = ttk.Entry(control_frame, textvariable=self.file_var, width=50)
        file_entry.grid(row=0, column=1, padx=5)
        
        browse_btn = ttk.Button(
            control_frame, 
            text="Browse", 
            command=self.browse_file,
            style='primary.TButton'
        )
        browse_btn.grid(row=0, column=2, padx=5)
        
        # Scan button
        scan_btn = ttk.Button(
            control_frame,
            text="Scan Errors",
            command=self.scan_log,
            style='danger.TButton'
        )
        scan_btn.grid(row=0, column=3, padx=5)
        
        # Theme selection
        ttk.Label(control_frame, text="Theme:").grid(row=1, column=0, sticky=tk.W, pady=(10,0))
        self.theme_var = tk.StringVar(value='darkly')
        
        # Get theme names from the Style instance we created
        theme_names = self.style.theme_names()
        theme_menu = ttk.OptionMenu(
            control_frame,
            self.theme_var,
            'darkly',
            *theme_names,
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
            height=20
        )
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags for styling
        self.result_text.tag_config("header", foreground="#4fc3f7", font=('Consolas', 11, 'bold'))
        self.result_text.tag_config("line_num", foreground="#ff7043")
        self.result_text.tag_config("error", foreground="#ff5252")
        self.result_text.tag_config("warning", foreground="#ffd740")
        self.result_text.tag_config("summary", foreground="#69f0ae", font=('Consolas', 10, 'bold'))
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        status_bar.pack(fill=tk.X, pady=(5,0))
    
    def browse_file(self):
        """Open file dialog to select log file"""
        filepath = filedialog.askopenfilename(
            title="Select Log File",
            filetypes=(("Log files", "*.log"), ("Text files", "*.txt"), ("All files", "*.*"))
        )
        if filepath:
            self.file_var.set(filepath)
            self.status_var.set(f"Selected: {filepath}")
            logging.info(f"Selected file: {filepath}")
    
    def scan_log(self):
        """Scan the log file for errors"""
        filepath = self.file_var.get()
        if not filepath:
            tk.messagebox.showwarning("Missing File", "Please select a valid log file.")
            logging.warning("Scan attempted without file selection")
            return

        try:
            found_lines = []
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    try:
                        if any(err_kw in line.lower() for err_kw in ERROR_KEYWORDS):
                            found_lines.append((line_num, line.strip()))
                    except UnicodeDecodeError as ude:
                        logging.error(f"Unicode decode error in line {line_num}: {ude}")
                        continue
                    except Exception as e:
                        logging.error(f"Error processing line {line_num}: {e}")
                        continue

            self.result_text.delete(1.0, tk.END)
            if found_lines:
                self.result_text.insert(tk.END, f"Found {len(found_lines)} potential error(s):\n\n", "header")
                for line_num, line in found_lines:
                    # Determine if it's an error or warning
                    tag = "error" if any(kw in line.lower() for kw in ["error", "fail", "fatal"]) else "warning"
                    
                    self.result_text.insert(tk.END, f"Line {line_num}: ", "line_num")
                    self.result_text.insert(tk.END, f"{line}\n\n", tag)
                
                self.result_text.insert(tk.END, f"\nTotal issues found: {len(found_lines)}", "summary")
                self.status_var.set(f"Scan complete. Found {len(found_lines)} issues.")
                logging.info(f"Scan completed with {len(found_lines)} issues found in {filepath}")
            else:
                self.result_text.insert(tk.END, "No error-related patterns found.", "header")
                self.status_var.set("Scan complete. No errors found.")
                logging.info(f"Scan completed - no issues found in {filepath}")

        except FileNotFoundError:
            error_msg = f"File not found: {filepath}"
            tk.messagebox.showerror("File Error", error_msg)
            logging.error(error_msg)
            self.status_var.set("Error: File not found")
        except PermissionError:
            error_msg = f"Permission denied when accessing: {filepath}"
            tk.messagebox.showerror("File Error", error_msg)
            logging.error(error_msg)
            self.status_var.set("Error: Permission denied")
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            tk.messagebox.showerror("File Error", error_msg)
            logging.error(error_msg, exc_info=True)
            self.status_var.set("Error: Processing failed")
    
    def change_theme(self, theme):
        """Change the application theme"""
        try:
            self.style.theme_use(theme)
            logging.info(f"Theme changed to {theme}")
        except Exception as e:
            logging.error(f"Theme switch error: {e}", exc_info=True)
            self.status_var.set("Theme change failed")

if __name__ == "__main__":
    root = tk.Tk()
    app = LogSeekerApp(root)
    root.mainloop()
