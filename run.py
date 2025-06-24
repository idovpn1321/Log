import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import logging
import os
from datetime import datetime
import re

# ====================== ENHANCED DETECTION CATEGORIES ======================
DETECTION_LEVELS = {
    "ERROR": {
        "color": "#FF5252",
        "keywords": ["error", "fail", "fatal", "crash", "exception", "timeout"],
        "patterns": [r"\berror\b", r"\bfail(?:ed|ure)?\b", r"\bfatal\b"]
    },
    "WARNING": {
        "color": "#FFD740",
        "keywords": ["warn", "unable", "cannot", "denied", "not found"],
        "patterns": [r"\bwarn(?:ing)?\b", r"\bcannot\b"]
    },
    "CODE_SMELL": {
        "color": "#FFAB91",
        "keywords": ["print(", "pass", "TODO", "FIXME"],
        "patterns": [r"print\s*\(", r"\bpass\b", r"\bTODO\b", r"\bFIXME\b"]
    },
    "RECOMMENDATION": {
        "color": "#80DEEA",
        "keywords": ["should", "recommend", "better", "improve"],
        "patterns": [r"\bshould\b", r"\brecommend\b", r"\bimprove\b"]
    }
}

class EnhancedLogSeeker:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        self.setup_logging()
        self.current_file = ""
        self.current_results = []
        
        # Windows-specific adjustments
        if os.name == 'nt':
            try:
                self.root.iconbitmap(default='icon.ico')
            except:
                pass

    def setup_logging(self):
        """Configure logging"""
        log_dir = os.path.join(os.environ.get('APPDATA', ''), 'EnhancedLogSeeker')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        logging.basicConfig(
            filename=os.path.join(log_dir, 'app.log'),
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info("Enhanced Log Seeker started")

    def setup_ui(self):
        """Enhanced UI with multi-level detection"""
        self.root.title("Enhanced Log Seeker v2.0")
        self.root.geometry("1000x700")
        
        # Main container
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Control panel
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=5)
        
        # File selection
        ttk.Label(control_frame, text="File:").grid(row=0, column=0, padx=5, sticky=tk.W)
        self.file_var = tk.StringVar()
        file_entry = ttk.Entry(control_frame, textvariable=self.file_var, width=60)
        file_entry.grid(row=0, column=1, padx=5)
        
        browse_btn = ttk.Button(
            control_frame, 
            text="Browse", 
            command=self.browse_file
        )
        browse_btn.grid(row=0, column=2, padx=5)
        
        # Detection level filter
        ttk.Label(control_frame, text="Filter:").grid(row=0, column=3, padx=5, sticky=tk.W)
        self.filter_var = tk.StringVar(value="ALL")
        filter_menu = ttk.Combobox(
            control_frame,
            textvariable=self.filter_var,
            values=["ALL"] + list(DETECTION_LEVELS.keys()),
            state="readonly",
            width=12
        )
        filter_menu.grid(row=0, column=4, padx=5)
        
        # Action buttons
        scan_btn = ttk.Button(
            control_frame,
            text="Analyze",
            command=self.analyze_file
        )
        scan_btn.grid(row=0, column=5, padx=5)
        
        self.copy_btn = ttk.Button(
            control_frame,
            text="Export Results",
            command=self.export_results,
            state='disabled'
        )
        self.copy_btn.grid(row=0, column=6, padx=5)
        
        # Results area
        results_frame = ttk.Frame(main_frame)
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        self.result_text = scrolledtext.ScrolledText(
            results_frame,
            wrap=tk.WORD,
            font=('Consolas', 10),
            height=25,
            padx=10,
            pady=10
        )
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags
        for level, config in DETECTION_LEVELS.items():
            self.result_text.tag_config(
                level,
                foreground=config["color"],
                font=('Consolas', 10, 'bold')
            )
        
        self.result_text.tag_config("HEADER", foreground="#0078D4", font=('Segoe UI', 12, 'bold'))
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready to analyze files")
        status_bar = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        status_bar.pack(fill=tk.X, pady=(5,0))
    
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
            self.current_file = filepath
            self.status_var.set(f"Selected: {os.path.basename(filepath)}")
    
    def analyze_file(self):
        """Enhanced analysis with multi-level detection"""
        filepath = self.file_var.get()
        if not filepath:
            messagebox.showwarning("Missing File", "Please select a file first.")
            return
        
        try:
            self.current_results = []
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    stripped_line = line.strip()
                    if not stripped_line:
                        continue
                    
                    detected_issues = self.detect_issues(stripped_line, line_num)
                    if detected_issues:
                        self.current_results.extend(detected_issues)
            
            self.display_results()
            self.copy_btn['state'] = 'normal'
        
        except Exception as e:
            self.handle_error(f"Analysis error: {str(e)}")
    
    def detect_issues(self, line, line_num):
        """Multi-level issue detection"""
        issues = []
        line_lower = line.lower()
        
        for level, config in DETECTION_LEVELS.items():
            # Check both keywords and patterns
            keyword_match = any(kw in line_lower for kw in config["keywords"])
            pattern_match = any(re.search(ptn, line_lower) for ptn in config["patterns"])
            
            if keyword_match or pattern_match:
                issues.append({
                    "line_num": line_num,
                    "line": line,
                    "level": level,
                    "message": self.generate_message(level, line)
                })
        
        return issues
    
    def generate_message(self, level, line):
        """Generate helpful messages for each detection level"""
        messages = {
            "ERROR": "This needs immediate attention",
            "WARNING": "This might cause problems",
            "CODE_SMELL": "This could be improved",
            "RECOMMENDATION": "Consider making this change"
        }
        return messages.get(level, "Found potential issue")
    
    def display_results(self):
        """Display filtered results"""
        self.result_text.delete(1.0, tk.END)
        
        if not self.current_results:
            self.result_text.insert(tk.END, "No issues found in the file", "HEADER")
            self.status_var.set("Analysis complete - No issues found")
            return
        
        filter_level = self.filter_var.get()
        filtered_results = [
            r for r in self.current_results 
            if filter_level == "ALL" or r["level"] == filter_level
        ]
        
        self.result_text.insert(tk.END, 
            f"Analysis Results for: {os.path.basename(self.current_file)}\n\n", 
            "HEADER")
        
        for issue in filtered_results:
            self.result_text.insert(tk.END, 
                f"[{issue['level']}] Line {issue['line_num']}: {issue['message']}\n",
                issue["level"])
            self.result_text.insert(tk.END, 
                f"   {issue['line']}\n\n",
                issue["level"])
        
        self.status_var.set(
            f"Found {len(filtered_results)} issues ({len(self.current_results)} total)"
        )
    
    def export_results(self):
        """Export results to clipboard or file"""
        if not self.current_results:
            messagebox.showwarning("No Results", "Nothing to export")
            return
        
        export_text = f"Enhanced Log Seeker Report\nFile: {self.current_file}\n\n"
        
        for issue in self.current_results:
            export_text += (
                f"[{issue['level']}] Line {issue['line_num']}: {issue['message']}\n"
                f"{issue['line']}\n\n"
            )
        
        # Copy to clipboard
        self.root.clipboard_clear()
        self.root.clipboard_append(export_text)
        
        # Also save to file
        save_path = os.path.join(
            os.path.dirname(self.current_file),
            f"analysis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
        
        try:
            with open(save_path, 'w') as f:
                f.write(export_text)
            messagebox.showinfo(
                "Export Complete", 
                f"Results copied to clipboard and saved to:\n{save_path}"
            )
        except Exception as e:
            messagebox.showinfo(
                "Export Partial", 
                f"Results copied to clipboard but couldn't save file:\n{str(e)}"
            )
    
    def handle_error(self, error_msg):
        """Error handling"""
        messagebox.showerror("Error", error_msg)
        self.status_var.set(error_msg)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, error_msg, "ERROR")

if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedLogSeeker(root)
    root.mainloop()
