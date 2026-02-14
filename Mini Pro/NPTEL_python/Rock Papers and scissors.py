print("Rock, Paper and scissors")

print()

print("Rock is Represented as R")
print("Paper is Represented as P")
print("Scissors is Represented as S")
print()


player_one={0:'R', 1:'P',3:'S'}
player_two={0:'P',2:'S',3:'R'}

def rock_paper_scissors(num1,num2,bit1,bit2):
    p1=int(int(num1[bit1])%3)
    p2=int(int(num2[bit2])%3)
    if player_one[p1] == player_two[p2]:
        print("Draw")
    elif player_one[p1] == "R" and player_two[p2] == "S":
        print("Player one wins!!")
    elif player_one[p1] == "R" and player_two[p2] == "P":
        print("Player two wins")
    elif player_one[p1] == "P" and player_two[p2] == "S":
        print("Player two wins!!")
    elif player_one[p1] == "P" and player_two[p2] == "R":
        print("Player one wins!!")
    elif player_one[p1] == "S" and player_two[p2] == "R":
        print("Player two wins!!")
    elif player_one[p1] == "S" and player_two[p2] == "P":
        print("Player one wins!!")

while 1:
    num1=input("Player 1, Enter your code = ")
    num2=input("Player 2, Enter your code = ")
    bit1=int(input("Player 1 , Enter your secret position = "))
    bit2=int(input("Player 2 , Enter your secret position = "))
    rock_paper_scissors(num1,num2,bit1,bit2)
    ch = input("Do you want to continue (y/n) : ")
    if ch=='n':
        break
