
import numpy as np

n = int(input())
info = []
for i in range(n):
    a, b, c = map(int,input().split())
    person = (a, b, c)
    info.append(person)
info.sort(reverse=True, key=lambda x:x[2])

world = np.zeros(n)
get_award = []
for i in range(n):
    if len(get_award) == 3:
        break
    if int(world[info[i][0]-1]) < 2:
        get_award.append(info[i])
        world[info[i][0]-1] += 1
    else : continue

for person in get_award:
    print("{} {}".format(person[0], person[1]))

    