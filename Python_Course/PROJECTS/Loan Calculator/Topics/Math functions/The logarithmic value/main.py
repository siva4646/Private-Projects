from math import log


x = int(input())
i = int(input())

if i < 2:
    print(round(log(x), 2))
else:
    print(round(log(x, i), 2))
