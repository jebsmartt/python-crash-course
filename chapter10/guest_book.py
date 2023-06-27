from pathlib import Path

loop_flag = 'Y'
guest_list = ""

while loop_flag == 'Y':
    name = input("What is your name? ")
    guest_list += (f"{name}\n")
    loop_flag = input("Would you like to add another name (Y/N)? ").upper()

path = Path('guest_book.txt')
path.write_text(guest_list)

