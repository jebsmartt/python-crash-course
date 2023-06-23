favorite_places = {
    'maggie' : ['outside','Paws n Pals',],
    'courtney' : ['Broadway'],
    'benton' : ['little gym','noni and papa\'s house','outside'],
}

for person in favorite_places:
    if len(favorite_places[person]) == 1:
        print(f"\n{person.title()}\'s favorite place is {favorite_places[person][0].title()}")
    else:
        print(f"\n{person.title()}'s favorite places are:")
        for places in favorite_places[person]:
            print(f"\t{places.title()}")
