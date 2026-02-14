c=int(input())

if c==1:
    def find_factors(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors


    num = int(input())
    print(find_factors(num),end="")

elif c==2:
    def common_factors(a, b):
        factors = []
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                factors.append(i)
        return factors

    num1 = int(input())
    num2 = int(input())

    print(common_factors(num1, num2),end="")

elif c==3:
    def factors_dict(n):
        result = {}
        for num in range(1, n + 1):
            factors = []
            for i in range(1, num + 1):
                if num % i == 0:
                    factors.append(i)
            result[num] = factors
        return result

    n = int(input())
    output = factors_dict(n)
    print(output,end="")



