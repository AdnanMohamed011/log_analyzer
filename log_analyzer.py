import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Analyze the logfile")
    parser.add_argument("logfile")
    parser.add_argument("--keyword", "-k")
    parser.add_argument("--date", "-d")
    args = parser.parse_args()

    logfile = args.logfile
    keyword = args.keyword
    date = args.date
    return logfile, keyword, date

def analyze_logs(logfile, keyword, date):
    try:
        with open(logfile, "r", encoding="utf-8") as f:
            error = 0
            warning = 0
            for i in f:
                line = i.lower()
                should_print = True

                if keyword and keyword.lower() not in line:
                    should_print = False
                if date and date not in line:
                    should_print = False
                
                if should_print == True:
                    print(i.strip())
                
                if "error" in line:
                    error += 1
                if "warn" in line:
                    warning += 1

            print(f"""
    --- Analysis Summary ---
    Total Errors: {error}
    Total Warnings: {warning}
    """)
    except FileNotFoundError as e:
        print(f"Error: The file '{logfile}' does not exist: {e}")

if __name__ == "__main__":
    logfile, keyword, date = parse_arguments()
    analyze_logs(logfile, keyword, date)
    pass