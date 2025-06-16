try:
    with open("sample.txt", "r") as file:
        for line in file.readlines():
            print(line)
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")