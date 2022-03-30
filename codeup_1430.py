
# import sys
# import numpy as np

# n = int(sys.stdin.readline().rstrip())
# d1 = sys.stdin.readline().rstrip()
# origin = np.array(d1.split())

# m = int(sys.stdin.readline().rstrip())
# d2 = sys.stdin.readline().rstrip()
# test = np.array(d2.split())

# for i in test:
#     if i in origin:
#         print(1, end = " ")
#     else : print(0, end = " ")


import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
d1 = np.zeros(10000000, dtype=int)
d1 = sys.stdin.readline().rstrip().split()

m = int(sys.stdin.readline().rstrip())
d2 = np.arange(100000, dtype=int)
d2 = sys.stdin.readline().rstrip().split()

for i in d2:
    if i in d1:
        print(1, end = " ")
    else : print(0, end = " ")



        