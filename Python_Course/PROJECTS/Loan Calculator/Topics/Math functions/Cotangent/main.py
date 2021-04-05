from math import cos, sin, pi

angle = int(input())
_pi = pi

angle = angle * (pi / 180)
print(round((cos(angle)) / (sin(angle)), 10))
