course = 'Python for Beginners'
# Calculate number of characters using len()
print(f'The length of course is: {len(course)}')


# upper()
course.upper() # Returns the string (course) with all of the characters uppercase. (Strings Only) This returns a value, and does not change the original string. 
print(course) # Prints course
print(course.upper()) # Prints course with all of the characters uppercase.

# find() CaSe SeNsItIvE: YES
course.find('P') # Returns the index of the first occurance of a value. If the value does not exist, it returns -1
print(f'The first occurance of \'P\' in course is at: {course.find("P")}') # 0
print(f'The first occurance of \'Z\' in course is at: {course.find("Z")}') # -1

# Passing through more than one character is allowed. find() returns the start of the string, and -1 if not found.
print(f'The first occurance of \'Beginners\' is at: {course.find("Beginners")}') # 0
print(f'The first occurance of \'Beginnerz\' is at: {course.find("Beginnerz")}') # -1

# replace() CaSe SeNsItIvE: YES
course.replace('Beginners', 'Absolute Beginners') # Returns the string, with the string inputted replaced. Does not replace if does not exist.
print(course) # Prints 'Python for Beginners'
print(course.replace('Beginners', 'Absolute Beginners')) # Prints 'Python for Absolute Beginners
print(course.replace('Beginnerz', 'Absolute Beginners')) # Prints 'Python for Beginners'
print('Python' in course) # True. Checks if 'Python' exists in course. Returns booleans.
print('python' in course) # False

# title()
# Turns the first letter of every word into a capital. Must be used when initiating a new string.
course_title = course.title()
print(course_title) # Python For Beginners