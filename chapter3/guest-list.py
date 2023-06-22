guest_list = ['Harry Potter', 'Hermione Granger', 'Ron Weasley', 'Dumbledore','Snape','Voldemort']

cant_attend = guest_list.pop(3)
guest_list.append('Hagrid')

def dinner_invitation(party):
    for i in party:
        print(f"{i}, would you like to come to dinner?")

# print(f"\n{cant_attend} is unable to attend because {guest_list[3]} killed {cant_attend}")
print("\nGood news, we found a larger table!")

guest_list.insert(0,'Fleur Delacour')
guest_list.insert(4, 'Draco Malfoy')
guest_list.append('Dobby')

print("\nThe bad news is that I can only invite two people to dinner")

def trim_guest_list(party):
    while len(party) > 2:
        i = 0
        sad_guest = guest_list.pop(i)
        print(f"{sad_guest} I'm sorry I can't invite you to dinner!\n")
    for g in party:
        print(f"{g} you are one of the two lucky guests!\n")
    
    while len(party) != 0:
        del party[0]
    
    print(party)

trim_guest_list(guest_list)


# dinner_invitation(guest_list)