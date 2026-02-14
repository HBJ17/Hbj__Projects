def binary_search(l,x,start,end):
    #base case: 1 element
    if start==end:
        if l[start]==x:
           return start
        else:
            return -1
    else:
        #divide into halves
        mid=(start+end)//2
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            return binary_search(l,x,start,mid-1)
        elif l[mid]<x:
            return binary_search(l,x,mid+1,end)
        else:
            print("not found")

l=[10,20,30,40,50,60]
x = int(input("Enter the number you want to search = "))
index = binary_search(l,x,0,len(l)-1)

if index==-1:
    print(x,"is not found")
else:
    print(x,"is found at position",index+1)



