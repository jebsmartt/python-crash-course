guest_list = ['Harry Potter', 'Hermione Granger', 'Ron Weasley', 'Dumbledore','Snape','Voldemort']

def dinner_invitation(party):
    for i in party:
        print(f"{i}, would you like to come to dinner?")

dinner_invitation(guest_list)
