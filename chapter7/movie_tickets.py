age = input("Hello! To know your movie ticket price, what is your age? ")
age = int(age)
ticket_price = 0


if age < 3:
    ticket_price = 0
elif age in range(3,13):
    ticket_price = 10
elif age > 12:
    ticket_price = 15

print(f"Based on your age of {age} your ticket price is ${ticket_price}")

