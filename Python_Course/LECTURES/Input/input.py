name = input('What is your name? ') # Receives input from the user. Unless method is used
                                    # Before it, it is a string
color = input('What is your favorite color? ')

print(name, 'likes', color)

birth_year = input('Birth Year: ')
age = 2021 - int(birth_year) # Explicit Type Conversion
# age = 2021 - birth_year will produce an error as birth_year is a string.
# int() String to int
# float() String to float
# bool() String to boolean
print(age)
print(type(birth_year)) # Prints type of birth_year, which is int

weight = int(input('Please input your weight (in pounds): '))
print('You weigh', round(weight / 2.205, 4), 'in kilograms')