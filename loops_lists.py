students = []

for i in range(int(input())):
    students.append([input(), float(input())])

print(students)

odd_numbers = [x for x in range(101) if x % 2 == 1]
print(odd_numbers)
print('''

''')

even_numbers = [x for x in range(101) if x % 2 == 0]
print(even_numbers)