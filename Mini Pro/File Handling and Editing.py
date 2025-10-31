# FILE HANDLING MODES DEMONSTRATION
# ---------------------------------

# Step 1️: Using 'w' mode (Write)
print("1️ 'w' mode: Write")
with open("demo.txt", "w") as f:
    f.write("Hello from write mode!\n")
    f.write("This overwrites the file if it exists.\n")
print("   ➤ Written to file using 'w' mode.\n")

# Step 2️: Using 'r' mode (Read)
print("2️ 'r' mode: Read")
with open("demo.txt", "r") as f:
    data = f.read()
    print("   ➤ File content:")
    print(data)
print()

# Step 3️: Using 'a' mode (Append)
print("3️ 'a' mode: Append")
with open("demo.txt", "a") as f:
    f.write("Appended line at the end!\n")
print("   ➤ Line appended.\n")

# Check file after append
with open("demo.txt", "r") as f:
    print("   ➤ Updated content:")
    print(f.read())
print()

# Step 4️: Using 'x' mode (Exclusive creation)
print("4️ 'x' mode: Create new file")
try:
    with open("newfile_demo.txt", "x") as f:
        f.write("This file is created using 'x' mode.")
    print("   ➤ newfile_demo.txt created successfully.\n")
except FileExistsError:
    print("   ⚠️ File already exists, cannot create again.\n")

# Step 5️: Using 'r+' mode (Read + Write)
print("5️ 'r+' mode: Read and Write")
with open("demo.txt", "r+") as f:
    print("   ➤ Before modification:")
    print(f.read())

    f.seek(0)  # Move cursor to beginning
    f.write("Modified!")  # Overwrite beginning part

    f.seek(0)
    print("\n   ➤ After modification:")
    print(f.read())
print()

# Step 6️: Using 'w+' mode (Write + Read)
print("6️ 'w+' mode: Write and Read (overwrites file)")
with open("demo.txt", "w+") as f:
    f.write("Completely new content from w+ mode!")
    f.seek(0)
    print("   ➤ After writing with w+:")
    print(f.read())
print("\n✅ Demonstration complete!")

