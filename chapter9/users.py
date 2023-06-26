class User:

    def __init__(self,first_name,last_name,birthday,city):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.city = city
        self.login_attempts = 0
    
    def describe_user(self):
        print(vars(self))

    def greet_user(self):
        print(f"Hello {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self, first_name, last_name, birthday, city):
        super().__init__(first_name, last_name, birthday, city)
        self.privileges = Privileges()

    
    
class Privileges:
    """The class should have one attribute, privileges, that 
    stores a list of strings as described in Exercise 9-7."""

    def __init__(self,privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        # print(f"\nThese are the admin user privileges for {self.first_name} {self.last_name}:")
        for p in self.privileges:
            print(f"- {p}")



