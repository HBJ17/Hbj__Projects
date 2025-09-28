print("GCD Finder")

x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))

if x < y:
    x, y = y, x

while y != 0:
    x, y = y, x % y

print("The GCD is:", x)




