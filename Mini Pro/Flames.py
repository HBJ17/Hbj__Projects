print("FLAMES")

print()

#remove the letters common in both names
def remove_matching_letter(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                c = l1[i]
                l1.remove(c)
                l2.remove(c)
                l = l1 + ["*"] + l2
                return [l,True]
    l = l1 + ["*"] + l2
    return [l, False]


#data about first person
n1 = input("Enter a name : ")
n1 = n1.lower()
n1 = n1.replace(" ","")

#data about the other person
n2 = input("Enter another name : ")
n2 = n2.lower()
n2 = n2.replace(" ","")

l1 = list(n1)
l2 = list(n2)

proceed = True
while proceed:
    # The list returned from the function
    ret_list = remove_matching_letter(l1, l2)

    # The list of letters is the first element of ret_list
    con_list = ret_list[0]

    # The boolean flag is the second element of ret_list
    proceed = ret_list[1]  # Corrected line!

    # The rest of your code is perfect
    star_index = con_list.index("*")
    l1 = con_list[:star_index]
    l2 = con_list[star_index + 1:]

count = len(l1) + len(l2)
result=["Friends","Love","Affection","Marriage","Enemy","Sister"]

split_index=(count%len(result))-1
while len(result)>1:
   split_index=(count%len(result))-1
   if split_index>=0:
      right=result[split_index+1:]
      left=result[:split_index]
      result=right+left
   else:
      result=result[:len(result)-1]

print(result[0])







