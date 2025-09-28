numbers = input()
number=numbers.split(",")
k = [str(num) for num in number]
z = max(reversed(k),key=len)
print(z)

