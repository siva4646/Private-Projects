# LOGICAL OPERATORS

has_high_income = True
has_good_credit = True
has_criminal_record = False


if has_high_income or has_good_credit:
    print('Eligible for loan')
else:
    print('Ineligible for loan')


# AND: If both conditions are True, return True
# OR: If one condition is True, return True
# NOT: If one variable is not equal to the other, return True

print(''' 


''')

if has_good_credit and not has_criminal_record:
    print('Eligible for loan')
else:
    print('Ineligible for loan')