# Class inheritance in Python 3 is done by passing the parent class as an argument to the child class
class Animal:
    def __init__(self, name):
        self.name = name

    def breath(self):
        print("inhale, exhale")


# The child class inherits all the methods and attributes of the parent class
class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print("moving in water")

    def breath(self):
        super().breath()
        print("doing this underwater")


memo = Fish("Memo")
memo.swim()
memo.breath()