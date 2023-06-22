current_users = ['bill123','HARRY_is_the_best','admin',
             'Username_Default','GLHF123','Peanuts77']

new_users = ['beatrix','admin', 'peanuts77','gracie']

current_users_toLower = []

for user in current_users:
    current_users_toLower.append(user.lower())

for user in new_users:
    if user.lower() in current_users_toLower:
        print(f"{user} is already in use. Please enter a new username.")
    else:
        print(f"Your username {user} was accepted.")
