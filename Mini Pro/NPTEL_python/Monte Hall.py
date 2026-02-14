import random

print("Welcome to the Monty Hall Game!")
print("There are 3 doors: Behind one is a CAR, behind the others are GOATS.")
print("You pick a door, then the host opens another door with a goat.")
print("You will then have the option to SWITCH or STAY.")

doors = [1, 2, 3]
car = random.choice(doors)

player_choice = int(input("Pick a door (1, 2, or 3): "))

possible_doors = [d for d in doors if d != player_choice and d != car]
host_opens = random.choice(possible_doors)
print("The host opens Door ...",host_opens,"It's a GOAT!")

remaining_doors = [d for d in doors if d != player_choice and d != host_opens]
switch_choice = remaining_doors[0]

decision = input("Do you want to SWITCH to the other unopened door? (yes/no): ").lower()

if decision == "yes":
    player_choice = switch_choice
    print(f"You switched to Door",player_choice)
else:
    print(f"You stayed with Door",player_choice)

if player_choice == car:
    print("🎉 Congratulations! You won the CAR!")
else:
    print("🐐 Oops, you got a GOAT.")
