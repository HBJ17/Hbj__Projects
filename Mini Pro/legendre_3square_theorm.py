def factors(n):
    if n == 0:
        return([0])
    factor_list = []
    for i in range(1,n+1):
        if n%i == 0:
            factor_list.append(i)
    return(factor_list)

def square(n):
    return(len(factors(n))%2 == 1)

def threesquares(n):
    for i in range(0,n+1):
        for j in range(i,n+1):
            if square(i) and square(j) and square(n-(i+j)):
                return(
                    True)
    return(False)

threesquares(8)