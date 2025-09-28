print("Dobble Game")
print()

import string

import random

symbols=list(string.ascii_letters)
card1=[0]*5
card2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)
print(pos1)
print(pos2)
samesymbol=random.choice(symbols)
symbols.remove(samesymbol)
while 1:
    if pos1 == pos2:
        card2[pos1] = samesymbol
        card1[pos1] = samesymbol
    else:
        card1[pos1] = samesymbol
        card2[pos2] = samesymbol
        c = card1[pos2] = random.choice(symbols)
        symbols.remove(c)
        d = card2[pos1] = random.choice(symbols)
        symbols.remove(d)

    i = 0
    while i < 5:
        if i != pos1 and i != pos2:
            alphabet1 = random.choice(symbols)
            symbols.remove(alphabet1)
            alphabet2 = random.choice(symbols)
            symbols.remove(alphabet2)
            card1[i] = alphabet1
            card2[i] = alphabet2
        i = i + 1

    print(card1)
    print(card2)
    print()
    ch = input("Enter the common symbol = ")
    if ch == samesymbol:
        print("True")
        c = int(input("press 0 to continue and 1 to end = "))
        if c == 0:
            print("Thankyou")
            break
    else:
        print("false")
        c = int(input("press 0 to continue and 1 to end = "))
        if c == 0:
            print('Thank you')
            break
