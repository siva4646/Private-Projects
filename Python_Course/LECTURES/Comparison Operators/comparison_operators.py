# COMPARISON OPERATORS

name = str(input()) # Initialize Variables
name_length = len(name)

if name_length < 3:
    print('Your name must be at least 3 characters.')
elif name_length > 50:
    print('Your name must be less than 50 characters.')
else:
    print('Name looks good!')

# >: Greater than
# <: Less than
# >=: Greater than or equal to
# <=: Less than or equal to
# ==: Equal to
# !=: Not equal to
