#!/usr/bin/env python3
"""The Comment Above the Code — prints the single entry line."""

LINE = "// The sleep(500) below is load-bearing: remove it and a thousand retries hit at once and checkout falls over."

def main():
    print(LINE)
    # The kit spec says the program writes its text to /output/entry.txt,
    # so write it there too when the directory exists (stdout stays exact).
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass

if __name__ == "__main__":
    main()
