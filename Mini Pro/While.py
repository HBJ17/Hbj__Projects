secret_word = "Dog"
guess = ""
number_of_try = 1
number_of_guess = 3
out_of_guess = False

while guess != secret_word and not out_of_guess:
    if number_of_try <= number_of_guess:
        guess = input("Enter your guess : ")
        number_of_try += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("you are out of chances.You LOSE!")
if guess == secret_word:
    print("You Win!!!!")



