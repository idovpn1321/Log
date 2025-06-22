
from termcolor import colored

FAIL_KEYWORDS = ["fail", "error", "crash", "recovery", "panic", "timeout"]

KEYWORDS = ["error", "fail", "boot", "recovery", "panic", "timeout", "crash"]

def highlight_keywords(lines):
    highlighted_lines = []
    for line in lines:
        for kw in KEYWORDS:
            if kw in line.lower():
                line = line.replace(kw, colored(kw, "red", attrs=["bold"]))
        highlighted_lines.append(line)
    return highlighted_lines
