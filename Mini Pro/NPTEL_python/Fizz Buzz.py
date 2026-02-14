
print("FizBuzz")

print()

r = int(input("Enter your range = "))

print()

def FizzBuzz(x):

    for i in range(1, r + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "= FizzBuzz")
        elif i % 3 == 0:
            print(i, "= Fizz")
        elif i % 5 == 0:
            print(i, "= Buzz")
        else:
            print(i)

FizzBuzz(r)



