
n = int(input())
d = list(map(int, input().split()))

     
sortvalues_asc = sorted(d)
sortvalues_desc = sorted(d, reverse=True)

same = 0
for num in d:
    if num == d[0]:
        same += 1
        
def f():
    if same == n:
        return print("섞임")
    if d == sortvalues_asc:
        print("오름차순")
    elif d == sortvalues_desc:
        print("내림차순")
    else: print("섞임")
    
f()
