used = []
last = ""

while True:
    word = input("Your word: ").lower()
    if word in used:
        print("Already used! Game over.")
        break
    if last and word[0] != last:
        print(f"Word must start with '{last}'. Game over.")
        break
    used.append(word)
    last = word[-1]


