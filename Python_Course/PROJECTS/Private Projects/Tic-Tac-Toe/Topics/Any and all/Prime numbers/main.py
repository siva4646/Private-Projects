import math

i = 1
prime_numbers = []
for x in range(1, 1001):

    if i % x == 1:
        prime_numbers.append(x)
    else:
         prime_numbers.append(i)

    i += 1

print(prime_numbers)