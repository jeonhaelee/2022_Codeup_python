
import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
d1 = sys.stdin.readline().rstrip()
origin = np.array(d1.split())

m = int(sys.stdin.readline().rstrip())
d2 = sys.stdin.readline().rstrip()
test = np.array(d2.split())

for i in test:
    if i in origin:
        print(1, end = " ")
    else : print(0, end = " ")



   


        