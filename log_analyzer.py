with open("sample.log", "r", encoding="utf-8") as f:
    reader = f
    for i in reader:
        print(i.strip())