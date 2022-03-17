d = []
for i in range(10):
    d.append(input().split())

now = 1
for x in range(1,9):
    for y in range(now,9):
        if int(d[x][y]) == 0:
            d[x][y] = 9
        if int(d[x][y+1]) == 1:
            now = y
            break
        if int(d[x][y+1]) == 2:
            d[x][y+1] = 9
            break
    if int(d[x+1][y]) == 2:
        d[x+1][y] = 9
        break
    
for i in range(10):
    for j in range(10):
        print(d[i][j], end = " ")
    print()