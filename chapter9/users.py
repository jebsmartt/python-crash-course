class User:

    def __init__(self,first_name,last_name,birthday,city):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.city = city
    
    def describe_user(self):
        print(vars(self))

    def greet_user(self):
        print(f"Hello {self.first_name}!")


user1 = User('Jeb','Smartt','10/24/1992','Renton')
user2 = User('Courtney','Smartt','3/12/1992','New York City')
user3 = User('Benton','Smartt','1/7/2021','Houston')

User.greet_user(user2)
User.greet_user(user3)
User.greet_user(user1)