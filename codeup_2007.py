
n = int(input())
d = list(map(int, input().split()))

asc = 0; desc = 0
for i in range(n-1):
    if d[i] < d[i+1]:
        asc += 1
    if d[i] > d[i+1]:
        desc += 1
    
if asc == 0:
    print("내림차순")
elif desc == 0:
    print("오름차순")
else: print("섞임")
    