vacation_poll_results = {}

prompt_name = "What is your name? "
prompt_location = "If you could visit one place in the world, where would you go? "

polling_active = True

while polling_active:
    name = input(prompt_name)
    location = input(prompt_location)
    vacation_poll_results[name] = location

    next_person = input("Would another person like to respond? (Yes / No) ")

    if next_person != 'Yes':
        polling_active = False

print("Here are the results of the vacation poll:")
for person,location in vacation_poll_results.items():
    print(f"\t{person.title()} would like to visit {location.title()}")