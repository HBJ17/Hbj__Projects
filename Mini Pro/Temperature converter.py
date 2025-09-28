print("TEMPERATURE CONVERTER")

print()

print("Choose the unit of the input value")

print()

print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")
print("4. Rankine")

print()

choice_1 = int(input("Choose any one option from (1-4) =  "))

print()

print("Choose To which unit do you want to convert the input value ")

print()

print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")
print("4. Rankine")

print()

choice_2 = float(input("Choose any one option from (1-4) =  "))

print()

N = float(input("Enter your input value = "))

print()

if choice_1 ==1 and choice_2 ==2:
    final = float(((N*9)/5) + 32)
    print("Answer is",final,"Fahrenheit")

elif choice_1 ==1 and choice_2 ==3:
    final = float(N + 273.15)
    print("Answer is",final,"Kelvin")

elif choice_1 ==1 and choice_2 ==4:
    final = float((((N*9)/5) + 32) + 459.67)
    print("Answer is",final,"Rankine")

elif choice_1 ==2 and choice_2 ==1:
    final = float(((N - 32)*5)/9)
    print("Answer is",final,"Celsius")

elif choice_1 ==2 and choice_2 ==3:
    final = float((((N -32)*5)/9) + 273.15)
    print("Answer is",final,"Kelvin")

elif choice_1 ==2 and choice_2 ==4:
    final = float(N + 459.67)
    print("Answer is",final,"Rankine")

elif choice_1 ==3 and choice_2 ==1:
    final = float(N - 273.15)
    print("Answer is",final,"Celsius")

elif choice_1 ==3 and choice_2 ==2:
    final = float((((N - 273.15)*9)/5) + 32)
    print("Answer is",final,"Fahrenheit")

elif choice_1 ==3 and choice_2 ==4:
    final = float(((((N - 273.15)*9)/5) + 32) + 459.67)
    print("Answer is",final,"Rankine")

elif choice_1 ==4 and choice_2 ==1:
    final = float(((N - 491.67)*5)/9)
    print("Answer is",final,"Celsius")

elif choice_1 ==4 and choice_2 ==2:
    final = float(N - 459.67)
    print("Answer is",final,"Fahrenheit")

elif choice_1 ==4 and choice_2 ==3:
    final = float((N*5)/9)
    print("Answer is",final,"Kelvin")
else:
    print("Please choose a valid option from (1-4) !!")


print()

print("Thank you for using the Converter!!")





