course = "Python's Course for Beginners" # Uses double quotes to allow the usage of single quotes before.
course_optimized = 'Python\'s Course for Beginners' # Uses \ which tells Python Interpreter that the next ' or " is part of the String 
print(course)
print(course_optimized)
print('''



''')
# This is an optimized way of printing multiple lines, without using multiple print() methods.
# Starting with """ or ''' will do this.
print('They both print the same thing, even though they are coded differently.')
# You can also have an 'f' at the start of the string, which stands for format. This allows you to include variables in the String without using ',' or '+'
f_example = f'This is a part of {course}'
# The {} (curly braces) represent a variable that should be in the String.
print(f_example)


# indexes

indexes_example = 'Python for Beginners'
print(indexes_example[0]) # Outputs 'P' because [0] is telling the Python Interpreter to get the first character in the indexes_example variable.
print(indexes_example[-1]) # This outputs the last value in the variable.
print(indexes_example[-2]) # This outpuds the second to last value in the variable
print(indexes_example[0:3]) # This outputs the values in the variable from the first to last index chosen, excluding the last #For example, printing [0:3] prints the first, second and third
print(indexes_example[:5]) # Prints the string from the start, to the index specified.
print(indexes_example[:]) # Prints the whole string.
