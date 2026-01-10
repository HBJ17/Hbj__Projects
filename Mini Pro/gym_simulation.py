import random
import time

workouts = {
    1: "10 Jumping Jacks",
    2: "15 Squats",
    3: "10 Push-ups",
    4: "20 High Knees",
    5: "30-second Plank",
    6: "15 Sit-ups"
}

print("WELCOME TO THE WORKOUT GAME")
print("Roll the dice and do the workout!")
print("-" * 35)

rounds = 5

for i in range(1, rounds + 1):
    input(f"\nRound {i} - Press ENTER to roll the dice")
    dice = random.randint(1, 6)
    print(f"You rolled: {dice}")
    print(f"Workout: {workouts[dice]}")
    time.sleep(1)

print("\n Game Over! Great job staying active!")
