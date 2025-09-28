def linear_search(n,x):
    element=[]
    for i in range(1,n):
        element.append(i)
    count=0
    flag = 0
    for i in element:
        count = count +1
        if i==x:
            print("Yess!! Found the number at position",str(i))
            flag = 1
            break

    if flag==0:
        print("Number not found!!!")

    print("Number of iterations =",str(count))

linear_search(100,33)






