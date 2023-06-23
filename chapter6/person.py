person_benton = {
    'first_name' : 'Benton',
    'last_name' : 'Smartt',
    'age' : 2,
    'city': 'Renton'
}

# for i in person:
#     print(f"{i} : {person.get(i)}")

person_erik = {
    'first_name' : 'Erik',
    'last_name' : 'Riddlebarger',
    'age' : 31,
    'city': 'Colorado Springs'
}

person_lake = {
    'first_name' : 'Lake',
    'last_name' : 'Smartt',
    'age' : 26,
    'city': 'Tacoma'
}

people = []

people.extend([person_benton,person_erik,person_lake])

for p in people:
    print(p)
    print("")

    