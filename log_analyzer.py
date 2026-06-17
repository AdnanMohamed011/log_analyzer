import sys
try:
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        for i in f:
            print(i.strip())

except FileNotFoundError:
    print("Error: The file 'filename' does not exist.")