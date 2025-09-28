def multiply(a: int, b: int) -> int:
    # Base case
    if b == 0:
        return 0

    # Recursive case: add 'a' b times
    return a + multiply(a, b - 1)


a = int(input())
b = int(input())

result = multiply(a, b)

print(result)