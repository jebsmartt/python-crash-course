guest_list = ['Harry Potter', 'Hermione Granger', 'Ron Weasley', 'Dumbledore','Snape','Voldemort']

cant_attend = guest_list.pop(3)
guest_list.append('Hagrid')

def dinner_invitation(party):
    for i in party:
        print(f"{i}, would you like to come to dinner?")

dinner_invitation(guest_list)
print(f"\n{cant_attend} is unable to attend because {guest_list[3]} killed {cant_attend}")
