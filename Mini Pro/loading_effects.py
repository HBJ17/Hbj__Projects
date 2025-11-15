import time

# dots animation
def loading_dots(message, dots=3, delay=0.4):
    for i in range(dots):
        print(f"{message}{'.' * (i + 1)}", end="\r", flush=True)
        time.sleep(delay)

    # clear the line
    print(" " * (len(message) + dots + 5), end="\r")


# rotating slash animation 
def loading_spinner(message, duration=2, delay=0.1):
    spinner = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    i = 0

    while time.time() < end_time:
        print(f"{message} {spinner[i % 4]}", end="\r", flush=True)
        time.sleep(delay)
        i += 1

    # clear the line
    print(" " * (len(message) + 5), end="\r")


# example usage
num1 = float(input("Enter first number: "))
loading_dots("Processing")

num2 = float(input("Enter second number: "))
loading_spinner("Processing")

loading_spinner("Calculating", duration=2)
result = num1 + num2
print("The sum is:", result)
