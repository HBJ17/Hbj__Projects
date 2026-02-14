import string


cipher_map = {}
data = ""

# Create the mapping (shift backward by 1)
for i in range(len(string.ascii_letters)):
    cipher_map[string.ascii_letters[i]] = string.ascii_letters[i-1]

with open("Data.txt") as file:
    while True:
        c = file.read(1)   # read one character
        if not c:          # end of file
            print("End of file")
            break

        if c in cipher_map:
            data += cipher_map[c]   # use mapped char
        else:
            data += c               # keep original if not in map

print(data)
