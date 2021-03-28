first_name = 'John'
last_name = 'Smith'
message = first_name + ' [' + last_name + '] is a coder'
# Concatonates the string, by adding ' ' and the first and last names, followed by 'is a coder'. 
print(message)
# Not optimal

message_optimized = f'{first_name} [{last_name}] is a coder'
print(message_optimized)