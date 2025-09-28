print("Magic Square")
n=int(input("Give the order of magic square = "))
def magic_square(n):
    magicsquare = [[0 for _ in range(n)] for _ in range(n)]

    i = n // 2
    j = n - 1

    num = n * n
    count = 1

    while(count<=num):
        if i == -1 and j == n:   # condition 1
            j = n - 2
            i = 0
        elif j == n:             # column out of bounds
            j = 0
        elif i < 0:              # row out of bounds
            i = n - 1

        if magicsquare[i][j] != 0:  # cell already filled
            i = i + 1
            j = j - 2
            continue
        else:
            magicsquare[i][j] = count
            count += 1

        i = i - 1
        j = j + 1

    # printing the square
    for i in range(n):
        for j in range(n):
            print(magicsquare[i][j], end=" ")
        print()

    print("Sum of each row, column, diagonal is =", (n * (n*n + 1)) // 2)

magic_square(n)
