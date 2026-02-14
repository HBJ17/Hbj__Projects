import turtle
import random


turtle.bgcolor("black")
seurat = turtle.Turtle()

width = 5
height = 7

seurat.penup()
list_color=["white","yellow","brown","red","blue","green","orange","pink","violet","grey","cyan"]

dot_distance = 25

seurat.setpos(-250,250)



def spiral(m, n):
    k = 0
    l = 0
    f = 0

    seurat.color("white")
    '''
    k is index of starting row
    l is index of starting column
    '''

    col = random.randint(0,10)
    seurat.color(list_color[col])

    while k<m and l<n :

        if f == 1:
            seurat.right(90)

        #printing the first row from the remaining rows
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[k][i] , end=" ")

        k = k + 1
        f =1

        seurat.right(90)
        col = random.randint(0, 10)
        seurat.color(list_color[col])
        #printing the last column from the remaining columns
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[i][n-1], end=" ")

        n = n - 1
        seurat.right(90)

        col = random.randint(0, 10)
        seurat.color(list_color[col])

        if k<m:
            #printing the last row from the remaining rows
            for i in range(n-1,l-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[m-1][i], end=" ")

            m = m - 1

        seurat.right(90)
        col = random.randint(0, 10)
        seurat.color(list_color[col])

        if l<n:
            #printing the first column from the remaining columns
            for i in range(m-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[i][l], end=" ")

            l = l + 1

spiral(20,20)
turtle.done()
