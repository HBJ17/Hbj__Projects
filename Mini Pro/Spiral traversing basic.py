# building the 4x4 matrix
a = []
count = 1
for i in range(4):
    row = []
    for j in range(4):
        row.append(count)
        count += 1
    a.append(row)

def spiral(m, n, a):
    k = 0  # starting row
    l = 0  # starting col

    while k < m and l < n:
        # print the first row from remaining rows
        for i in range(l, n):
            print(a[k][i], end=" ")
        k += 1

        # print the last column from remaining columns
        for i in range(k, m):
            print(a[i][n-1], end=" ")
        n -= 1

        # print the last row from remaining rows
        if k < m:
            for i in range(n-1, l-1, -1):
                print(a[m-1][i], end=" ")
            m -= 1

        # print the first column from remaining columns
        if l < n:
            for i in range(m-1, k-1, -1):
                print(a[i][l], end=" ")
            l += 1


spiral(4, 4, a)
