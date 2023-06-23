toppings = []
topping = ""
prompt = "Enter a topping to add to your pizza (or \"Quit\" to exit):"


while topping != "Quit":
    # topping = input("Enter a topping to add to your pizza: ")
    topping = input(prompt).title()
    if topping != "Quit":
        toppings.append(topping)
    print(toppings)

