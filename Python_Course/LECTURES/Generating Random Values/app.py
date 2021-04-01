import random

for i in range(3):
    print(random.randint(10, 20)) # Generates 3 random ints from 10 to 20

print('''



''')

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members) # Randomly picks an item from members
print(leader)

print('''


''')


class Dice:
    def roll(self):
        return (random.randint(1, 6), random.randint(1, 6))


dice = Dice()
print(dice.roll())