def multiply(a: int, b: int) -> int:
    # Base case
    if b == 0:
        return 0
    elif a == 0:
        return 0

    # Recursive case: add 'a' b times
    return a + multiply(a, b - 1)


a = int(input("Enter a = "))
b = int(input("Enter b = "))

result = multiply(a, b)

print(result)
