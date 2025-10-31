with open("file.txt", "w") as f:
    f.write("Hello from Python!\n")

with open("file.txt", "r") as f:
    content = f.read()
    print(content)
