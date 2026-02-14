numbers = input()
number=numbers.split(" ")
k = [float(num) for num in number]
print(k)
print(",".join(str(int(num)) for num in k))