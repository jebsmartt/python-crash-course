person = {
    'first_name' : 'Benton',
    'last_name' : 'Smartt',
    'age' : 2,
    'city': 'Renton'
}

for i in person:
    print(f"{i} : {person.get(i)}")
    