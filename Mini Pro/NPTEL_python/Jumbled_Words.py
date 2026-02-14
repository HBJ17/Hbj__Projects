print('JUMBLED WORDS')

print()

import random

def choose():
    words=["crystal","planet","shadow","anchor","whisper","jungle","fabric","candle","puzzle","mirror","galaxy","castle","thunder","rocket","ladder","island","silver","breeze","magnet","crown"]
    word=random.choice(words)
    return word

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def Thankyou(p1,p2,pp1,pp2):
    print("Thank you for playing!!")
    print(p1,', your total score is',pp1)
    print(p2, ', your total score is', pp2)
    return Thankyou

print()

def play():
    p1 =input("Player 1, Enter your name = ")

    print()

    p2 =input("Player 2, Enter your name = ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        if turn%2==0:
            print("Hey",p1,", its your turn")
            print()
            ans = input("Enter your answer = ")
            print()
            if ans==picked_word:
                print("Congrats",p1,"You earn a point")
                print()
                pp1=pp1+1
                print(p1,"Points =",pp1)
                print()
            else:
                print("Oopsie!, Your wrong")
                print()
                print(p1, "Points =", pp1)
                print()
            c= int(input("Press 1 to continue and 0 to finish (0/1) "))
            print()
            if c==0:
                Thankyou(p1,p2,pp1,pp2)
                break
        else:
            print("Hey", p2, ", its your turn")
            print()
            ans = input("Enter your answer = ")
            print()
            if ans == picked_word:
                print("Congrats", p2, "You earn a point")
                print()
                pp2 = pp2 + 1
                print(p2, "Points =", pp2)
                print()
            else:
                print("Oopsie!, Your wrong")
                print()
                print(p2, "Points =", pp2)
                print()
            c=int(input("Press 1 to continue and 0 to finish (0/1) "))
            print()
            if c==0:
                Thankyou(p1,p2,pp1,pp2)
                break



        turn=turn+1
play()







