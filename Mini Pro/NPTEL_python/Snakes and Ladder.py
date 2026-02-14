from PIL import Image
import random

end = 100

def show_board():
    img = Image.open('D:\Studies\PycharmProjects\PythonProject\Images\slb image.jpg')
    img.show()

def check_ladder(points):
    if points==4:
        print("Ladder")
        return 25
    elif points==13:
        print("Ladder")
        return 46
    elif points==42:
        print("Ladder")
        return 63
    elif points==50:
        print("Ladder")
        return 69
    elif points==74:
        print("Ladder")
        return 92
    elif points==62:
        print("Ladder")
        return 81
    else:
        # not a ladder
        return points


def check_snake(points):
    if points==40:
        print("snake!!")
        return 3
    elif points==27:
        print("snake!!")
        return 5
    elif points==43:
        print("snake!!")
        return 18
    elif points==66:
        print("snake!!")
        return 45
    elif points==54:
        print("snake!!")
        return 31
    elif points==89:
        print("snake!!")
        return 53
    elif points==95:
        print("snake!!")
        return 77
    elif points==99:
        print("snake!!")
        return 41
    else:
        #not a snake
        return points

def reached_end(points):
    if points==end:
        return True
    else:
        return False

def play():
    #input player 1 name
    p1_name = input('Player 1, Enter your name = ')
    #input player 2 name
    p2_name = input('Player 2, Enter your name = ')

    #initial points of player 1
    pp1=0
    #initial points of player 2
    pp2=0

    turn = 0

    while(1):
        if turn%2==0:
            #player 1 turn
            print("Player 1, Its your turn.")
            #players choice
            c= int(input("Enter 1 to continue and 0 to quit = "))
            if c==0:
                print(p1_name,", scored",pp1)
                print(p2_name, ", scored", pp2)
                print("Quiting the game , Thank you for playing")
                break

            #generate random number
            dice = random.randint(1,6)
            print('Dice showed',dice)
            pp1= pp1 + dice

            pp1 = check_ladder(pp1)

            pp1 = check_snake(pp1)

            #check if player points is beyond limit
            if pp1 > end:
                pp1=end

            print("player 1 score =",pp1)

            if reached_end(pp1):
                print(p1_name,"You won the game")
                break

        else:
            #player 2 turn
            print("Player 2, Its your turn.")
            #players choice
            c= int(input("Enter 1 to continue and 0 to quit = "))
            if c==0:
                print(p1_name,", scored",pp1)
                print(p2_name, ", scored", pp2)
                print("Quiting the game , Thank you for playing")
                break

            #generate random number
            dice = random.randint(1,6)
            print('Dice showed',dice)
            pp2= pp2 + dice

            pp2 = check_ladder(pp2)

            pp2 = check_snake(pp2)

            #check if player points is beyond limit
            if pp2 > end:
                pp2=end

            print("player 2 score =",pp2)

            if reached_end(pp2):
                print(p2_name,"You won the game")
                break

        #increment the number of turns
        turn = turn + 1

show_board()

play()


