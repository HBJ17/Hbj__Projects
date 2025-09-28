print("Bubble sorting")
print()

def bubble(a):
    n = len(a)

    for i in range(n):
        for j in range(n-i-1):  #1 is subtracted to maintain the index number count
            if a[j]>a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp

a = [1,6,5,8,3,9,3]
bubble(a)

for i in a:
    print(i)
