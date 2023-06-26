from random import randint

class Die:
    '''TIY 9-13'''

    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        times = input(f"\nHow many times would you like to roll? ")
        times = int(times)
        while times > 0:
            print(randint(1,self.sides))
            times -= 1


six_die = Die()
ten_die = Die(10)
twenty_die = Die(20)

Die.roll_die(six_die)
Die.roll_die(ten_die)
Die.roll_die(twenty_die)