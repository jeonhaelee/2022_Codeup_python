

from cmath import pi


def circle(r):
    return 3.14 * pow(r,2)

r = int(input())
print("%.2f"%circle(r))