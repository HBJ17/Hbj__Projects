matrix = []

print("Enter values for a 3x3 matrix:")

print()

for i in range(3):          # 3 rows
    row = []
    for j in range(3):      # 3 columns
        value = int(input(f"Enter value for position ({i+1},{j+1}): "))
        row.append(value)
    matrix.append(row)

print("Your 3x3 Matrix is:")
for row in matrix:
    print(*row)   # *row prints numbers without brackets
