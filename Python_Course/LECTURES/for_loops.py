# FOR LOOPS

for item in 'Python':
    print(item)

# Iterates through the string 'Python' and prints
# Every element.

print('''


''')

# for item in iterable:
#   do something..

for item in ['Mosh', 'John', 'Sarah']:
    print(item)

# Iterates through the list containing names, and prints each of them.

for item in range(10):
    print(item)

print('''


''')
# Does the inside blocks of code n times, excluding the last, starting from 0.
# You can also use two elements, which dictate the loop to start at n, and end at j.
# Lastly, with three elements, you can select how much k increases with the third element.

for item in range(5, 10):
    print(item)
# 5, 6, 7, 8, 9

print('''

''')

n = 5
j = 10
k = 2
for item in range(n, j, k):
    print(item)
# 5, 7, 9

total = 0
prices = [10, 20, 30]
for price in prices:
    total += price
print(total)