from pathlib import Path
import json



def input_number():
    
    number_input = input("What is your favorite number? ")
    number_input = str(number_input)

    contents = json.dumps(number_input)
    return contents

def favorite_number():
    name_input = input("What is your name? ")
    name_input = str(name_input)

    path = Path(f"{name_input}.txt")
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        print(f"Hello {name_input}. We remember that your favorite number is {favorite_number}")
    else:
        
        path.write_text(input_number())
        print(f"We'll remember your number next time, {name_input}")


favorite_number()    
