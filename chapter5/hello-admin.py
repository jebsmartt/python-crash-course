usernames = ['bill123','harry_is_the_best','admin',
             'username_default','ghlf123','peanuts77']


if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
