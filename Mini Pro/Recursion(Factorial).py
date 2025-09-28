def factorial(n):
    product = 1

    #Iterative version
    '''
    for i in range(1,n+1):
        product = product * i   
    return product
    '''

    #recursive version
    #fact(n)=n*fact(n-1)

    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n = int(input("Enter a Positive number = "))
if n<0:
    print("Factorial is not defined for negative number")
else:
    f=factorial(n)
    print('factorial of',n,"is",f)
    