
import sys
import argparse
from utils.parser import parse_logs
from utils.highlighter import highlight_keywords

def main():
    parser = argparse.ArgumentParser(description="Zuan Log Analyzer CLI")
    parser.add_argument("files", nargs="+", help="Log file(s) to analyze")
    parser.add_argument("--pattern", help="Pattern to search for (e.g., bootloop)", required=False)
    args = parser.parse_args()

    for file_path in args.files:
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read()
            parsed = parse_logs(content)
            if args.pattern:
                parsed = [line for line in parsed if args.pattern in line]
            highlighted = highlight_keywords(parsed)
            for line in highlighted:
                print(line)

if __name__ == "__main__":
    main()
