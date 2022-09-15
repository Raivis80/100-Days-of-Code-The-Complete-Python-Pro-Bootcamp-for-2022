## OOP classes and objects

class User:
    # __init__ is a constructor method
    def __init__(self, name, user_id):
        self.name = name
        self.id = user_id
        self.followers = 0
        self.following = 0

    # Methods are functions defined inside the body of a class
    def follow(self, user):
        user.followers += 1
        self.following += 1
        print(f"{self.name} is now following {user.name}")


user1 = User("John", 123)
user2 = User("Jane", 456)

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)