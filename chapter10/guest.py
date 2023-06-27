from pathlib import Path

user_input = input("What is your name? ")

path = Path('guest.txt')
path.write_text(user_input)