from random import randint, choice

class LottoTicket:
    """Represents a lottery ticket"""

    def __init__(self):
        self.winning_sequence = []

    def create_winning_sequence(self):
        """Create a bank of 10 numbers and 5 letter from
        which the winning sequence can be selected from"""
        number_bank = []
        letter_bank = []
        while len(number_bank) < 10:
            number_bank.append(str(randint(0,9)))
        while len(letter_bank) < 5:
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            letter_bank.append(choice(alphabet))
        
        # Create the superset of numbers and letters
        combined_bank = number_bank + letter_bank

        """Take items from combined bank list and add to 
        winning sequence until winning sequence has 
        4 items"""
        while len(self.winning_sequence) < 4:
            selection = choice(combined_bank)
            self.winning_sequence.append(selection)
            combined_bank.remove(selection)


    def announce_winner(self):
        message = "Any ticket matching these 4 numbers or letters wins a prize: "
        print(message)
        print(f"\t{self.winning_sequence}")

class MyTicket:

    def __init__(self,char1,char2,char3,char4):
        self.char1 = str(char1)
        self.char2 = str(char2)
        self.char3 = str(char3)
        self.char4 = str(char4)
        self.my_numbers = [str(char1),str(char2),str(char3),str(char4)]
        self.winner = False

    def did_i_win(self,winning_numbers):
        print(f"\nHere are your numbers {self.my_numbers}")
        if sorted(self.my_numbers) == sorted(winning_numbers):
            print("You Won!")
            self.winner = True
        else:
            print("You did't win")

    def games_til_win(self):
        game_counter = 0
        winning_numbers = LottoTicket()
        winning_numbers.create_winning_sequence()

        while self.winner == False:
            game_counter += 1
            if sorted(self.my_numbers) == sorted(winning_numbers.winning_sequence):
                print("\nYou Won!")
                self.winner = True
            winning_numbers.winning_sequence = []
            winning_numbers.create_winning_sequence()
            
        print(f"We found a winner, and it only took {game_counter} trys.")
    
    

# Lotto1 = LottoTicket()
# Lotto1.create_winning_sequence()
# Lotto1.announce_winner()

a_ticket = MyTicket('c',3,1,2)

a_ticket.games_til_win()



        