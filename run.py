# ====================== ERROR DETECTION KEYWORDS ======================
ERROR_KEYWORDS = [
    "fail", "error", "unable", "not found", "exception",
    "cannot", "no such", "permission denied", "timeout",
    "segfault", "panic", "missing", "denied", "abort",
    "fatal", "unreachable", "not registered", "unresolved",
    "crash", "corrupt", "invalid", "failed", "warning"
]

# Add this at the beginning of your script (after imports)
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='zuanlogseeker_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def scan_log():
    """Scan log file for errors and display results."""
    filepath = file_var.get()
    if not filepath:
        ttk.dialogs.Messagebox.show_warning("Missing File", "Please select a valid log file.")
        logging.warning("User attempted to scan without selecting a file")
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

        result_text.delete(1.0, ttk.END)
        if found_lines:
            result_text.insert(ttk.END, f"Found {len(found_lines)} potential error(s):\n\n", "header")
            for line_num, line in found_lines:
                result_text.insert(ttk.END, f"Line {line_num}: ", "line_num")
                result_text.insert(ttk.END, f"{line}\n\n")
            result_text.insert(ttk.END, f"\nTotal errors found: {len(found_lines)}", "summary")
            status_var.set(f"Scan complete. {len(found_lines)} error lines found.")
            logging.info(f"Scan completed successfully with {len(found_lines)} errors found in {filepath}")
        else:
            result_text.insert(ttk.END, "No error-related patterns found.")
            status_var.set("Scan complete. No errors found.")
            logging.info(f"Scan completed - no errors found in {filepath}")

    except FileNotFoundError:
        error_msg = f"File not found: {filepath}"
        ttk.dialogs.Messagebox.show_error("File Error", error_msg)
        logging.error(error_msg)
    except PermissionError:
        error_msg = f"Permission denied when accessing: {filepath}"
        ttk.dialogs.Messagebox.show_error("File Error", error_msg)
        logging.error(error_msg)
    except Exception as e:
        error_msg = f"Unexpected error processing file: {str(e)}"
        ttk.dialogs.Messagebox.show_error("File Error", error_msg)
        logging.error(error_msg, exc_info=True)

# Update your theme switching function:
def change_theme():
    try:
        selected_theme = theme_var.get()
        ttk.Style().theme_use(selected_theme)
        logging.info(f"Theme changed to {selected_theme}")
    except Exception as e:
        error_msg = f"Theme switch error: {e}"
        logging.error(error_msg, exc_info=True)
        # Optionally show this to user if you want:
        # ttk.dialogs.Messagebox.show_warning("Theme Error", "Could not change theme")
