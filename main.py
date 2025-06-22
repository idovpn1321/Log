import sys
import argparse
from untils.parser import parse_logs
from untils.highlighter import highlight_keywords, FAIL_KEYWORDS

def main():
    parser = argparse.ArgumentParser(description="Zuan Log Analyzer CLI")
    parser.add_argument("files", nargs="+", help="Log file(s) to analyze")
    parser.add_argument("--pattern", help="Custom pattern to filter (optional)")
    parser.add_argument("--fail-only", action="store_true", help="Only show failure-related lines")
    args = parser.parse_args()

    for file_path in args.files:
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read()
            lines = parse_logs(content)

            if args.fail_only:
                lines = [line for line in lines if any(k in line.lower() for k in FAIL_KEYWORDS)]
            elif args.pattern:
                lines = [line for line in lines if args.pattern.lower() in line.lower()]

            highlighted = highlight_keywords(lines)
            for line in highlighted:
                print(line)

if __name__ == "__main__":
    main()
