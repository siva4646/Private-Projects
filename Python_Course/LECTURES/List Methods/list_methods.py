numbers = [5, 2, 1, 7, 4]
numbers.insert(0, 20) # Inserts element at an index
numbers.append(20) # Inserts element at the end
numbers.pop() # Removes last element
print(numbers)
print(50 in numbers)
print(f'There are {numbers.count(20)} 20s in {numbers}')
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)


# Remove duplicates in a list
duplicates_in_list = [20, 5, 20, 19, 50, 50]
for item in duplicates_in_list:
    if duplicates_in_list.count(item) > 1:
        duplicates_in_list.remove(item)
print(duplicates_in_list)