from math import sqrt

a = int(input())
b = int(input())
c = int(input())

p = (a + b + c) / 2
s = sqrt(p * ((p - a) * (p - b) * (p - c)))
print(s)

# S=p(p−a)(p−b)(p−c)‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾√
