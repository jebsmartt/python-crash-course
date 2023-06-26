import users


user1 = users.Admin('Jeb','Smartt','10/24/1992','Renton')
# user2 = User('Courtney','Smartt','3/12/1992','New York City')
# user3 = User('Benton','Smartt','1/7/2021','Houston')

# # User.greet_user(user2)
# # User.greet_user(user3)
users.User.greet_user(user1)

# # user1.increment_login_attempts()
# # user1.increment_login_attempts()
# # print(user1.login_attempts)
# # user1.reset_login_attempts()
# # print(user1.login_attempts)

user1.privileges.privileges = ["can add post", "can delete post", "can ban user"]

user1.privileges.show_privileges()