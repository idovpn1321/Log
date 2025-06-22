---

## 🛠️ Usage Guide

Zuan Log Analyzer is a CLI-based tool that helps you extract, filter, and highlight important log information — especially errors, crashes, and bootloop traces — from raw Android logs like `logcat`, `dmesg`, etc.

---

### ▶️ Basic Command

```bash
python3 main.py <log_file1> <log_file2> ...

Supports one or multiple log files.

Will print all lines, with important keywords highlighted in red.



---

🎯 Filter by Custom Pattern

python3 main.py logcat.txt --pattern "bootloop"

Shows only the lines that contain the specified keyword (case-insensitive).

Useful for searching a specific error message, tag, or event.



---

🚨 Show Only Failure-Related Lines

python3 main.py logcat.txt --fail-only

Filters output to only show lines that contain critical failure-related keywords, such as:

fail

error

crash

recovery

panic

timeout


These are defined in the tool's FAIL_KEYWORDS list and can be modified manually in utils/highlighter.py.



---

🧪 Quick Testing with Dummy Logs

To simulate and test the tool:

echo -e "Booting device...\nSystem crash detected\nRestarting to recovery" > test.txt
python3 main.py test.txt --fail-only


---

📌 All Available Options

Option	Description

<files>	One or more log files to process
--pattern	Filter logs using a custom string/pattern (case-insensitive)
--fail-only	Only show lines with known failure keywords


You can combine options:

python3 main.py log.txt --pattern crash --fail-only

⚠️ In that case, the --fail-only filter will take precedence.


---

🧼 Highlighting Behavior

All important terms like error, fail, recovery, etc., will be automatically colored red using the termcolor module.

Output is designed to be terminal-friendly.



---

💾 Saving the Output

To save the filtered results to a file:

python3 main.py logcat.txt --fail-only > results.txt


---

❓ When Should You Use This?

You're debugging Android system issues like bootloops, crashes, or app force closes.

You want to extract only the failure lines from a huge log file.

You prefer using Termux or any minimal terminal without heavy GUI tools.



---

🧱 Dependencies

Python 3.x

termcolor


Install with:

pip install termcolor


---

🗃️ Folder Structure

ZuanLogAnalyzer/
├── main.py                 # Main CLI entry point
└── utils/
    ├── __init__.py
    ├── parser.py           # Splits logs into lines
    └── highlighter.py      # Highlights & filters keywords


---

If you need a versioned CLI flag like --version, or want to convert this tool into a pip-installable Python package (setup.py etc.), I can help you modularize and package it as well.

---

Let me know if you'd like a badge section (`GitHub Actions`, `PyPI`, etc.), a license section, or even a demo GIF previewing the tool in action — those are nice touches for public GitHub projects.

