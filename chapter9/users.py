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



user1 = Admin('Jeb','Smartt','10/24/1992','Renton')
user2 = User('Courtney','Smartt','3/12/1992','New York City')
user3 = User('Benton','Smartt','1/7/2021','Houston')

# User.greet_user(user2)
# User.greet_user(user3)
# User.greet_user(user1)

# user1.increment_login_attempts()
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.reset_login_attempts()
# print(user1.login_attempts)

user1.privileges.privileges = ["can add post", "can delete post", "can ban user"]

user1.privileges.show_privileges()