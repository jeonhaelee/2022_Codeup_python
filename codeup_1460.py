num = int(input())
nums = num*num

d = []
for i in range(nums):
    d.append(i+1)

for i in range(nums):
    print(d[i], end = " ")
    if (i+1) % num == 0:
        print()
        
