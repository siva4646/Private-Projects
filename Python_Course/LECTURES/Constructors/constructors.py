class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hello, my name is {self.name}')


# point1 = Point()
# print(point1.x) AttributeError
me = Person(input())
me.talk()