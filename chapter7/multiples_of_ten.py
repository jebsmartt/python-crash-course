number = input("Please enter a whole number: ")
number = int(number)

if number % 10 == 0:
    print(f"The number you entered, {number}, is divisible by 10.")
elif number % 10 > 0:
    print(f"The number you entered, {number}, is not divisible by 10.")
else:
    print("Please enter a number")