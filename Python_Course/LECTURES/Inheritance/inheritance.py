class Mamal:
    def walk(self):
        print('Walk')

class Dog(Mamal):
    def bark(self):
        print('Bark')


class Cat(Mamal):
    pass


Labrador = Dog()
Labrador.walk()
Labrador.bark()