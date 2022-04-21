

n = int(input())

star = "*"
space = " "
space_cnt = n-1
space_cnt2 = 0

for i in range(n-1):
    space1 = space * space_cnt
    space2 = space * space_cnt2
    print(space1 + star + space2 + star)
    space_cnt -= 1
    space_cnt2 += 2

space1 = space * space_cnt
space2 = space * space_cnt2
print(space1 + star + space2 + star)

for i in range(n):
    space1 = space * space_cnt
    space2 = space * space_cnt2
    print(space1 + star + space2 + star)
    space_cnt += 1
    space_cnt2 -= 2
