n = int(input())
d = list(map(int,input().split()))

for i in range(n):
    print("{}:".format(i+1), end = " ")
    for j in range(n):
        if i == j:
            continue
        if d[i] > d[j]:
            print('>', end = " ")
        elif d[i] < d[j]:
            print('<', end = " ")
        else : print('=', end = " ")
    print()