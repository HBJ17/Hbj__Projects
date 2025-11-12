import random
import time

def musical_chairs():
    print(" Welcome to the Musical Chairs Game! ")
    players = []

    n = int(input("Enter the number of players: "))
    for i in range(1, n + 1):
        name = input(f"Enter player {i} name: ")
        players.append(name)

    print()
    print("Let's start the game!")

    r = 1

   
    while len(players) > 1:
        print()
        print(f"    Round {r}    ")
        print("Music is playing... ")
        time.sleep(random.randint(2, 10))  

        print("Music stopped!")

        e = random.choice(players)
        players.remove(e)
        print(f"{e} couldn't find a chair and is eliminated!")

        print(f"Players left: {', '.join(players)}")
        r += 1
        time.sleep(2)

    print()
    print("The winner is:", players[0], "! Congratulations!")


musical_chairs()

