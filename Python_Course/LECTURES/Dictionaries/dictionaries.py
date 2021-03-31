# Name: John Smith
# EMail: john@appleseed.com
# P/N: 0403866920

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["birth_date"] = "Jan 1 1980"
# print(customer["nam"]) KeyError: "nam"
print(customer["name"]) # John Smith
# print(customer["Name"]) KeyError: "Name"
print(customer.get("name")) # John Smith
print(customer.get("nam")) # None
print(customer.get("birth_date"))

print('''


''')

numbers = {

    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero"
}

numbers_word = ''
number = input("Phone: ")
for x in number:
    word = numbers[int(x)]
    numbers_word += word + ' '
numbers_word += '!'
print(numbers_word)