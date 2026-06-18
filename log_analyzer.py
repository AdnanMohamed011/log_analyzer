import sys
try:
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        error = 0
        warning = 0
        for i in f:
            line = i.lower()
            if "error" in line:
                error += 1
            if "warn" in line:
                warning += 1
            if len(sys.argv) > 2:
                if sys.argv[-1].lower() in line:
                    print(i.strip())
        
            elif len(sys.argv) == 2:
                print(i.strip())
        print(f"""
--- Analysis Summary ---
Total Errors: {error}
Total Warnings: {warning}
""")
except FileNotFoundError:
    print(f"Error: The file '{sys.argv[1]}' does not exist.")