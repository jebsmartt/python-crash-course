from pathlib import Path
import json
    
def get_stored_user_data(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_data = json.loads(contents)
        return user_data
    else:
        return None

def get_new_user_data(path):
    """Prompt for a new user data."""
    username = input("What is your name? ")
    city = input("What city do you live in? ")
    color = input("What is your favorite color? ")

    user_data = {
        'username':username,
        'city':city,
        'color':color,
    }

    contents = json.dumps(user_data)
    path.write_text(contents)
    return user_data

def greet_user():
    """Greet the user by name."""
    path = Path('user_data.json')
    user_data = get_stored_user_data(path)

    if user_data:
        print(f"Welcome back, {user_data['username']}!")
        print(f"\tYou live in {user_data['city']}")
        print(f"\tYour favorite color is {user_data['color']}")
    else:
        user_data = get_new_user_data(path)
        print(f"We'll remember you when you come back, {user_data['username']}!")

greet_user()