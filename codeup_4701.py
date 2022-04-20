
import sys
input = sys.stdin.readline 

n = int(input())
d = sorted(list(map(int,input().split())))

head = 0
rear = n-1

answer = abs(d[head] + d[rear])
idx_1 = head
idx_2 = rear

while head < rear:
    sub = d[head] + d[rear]
    if abs(sub) < answer:
        answer = abs(d[head] + d[rear])
        idx_1 = head
        idx_2 = rear
    if answer == 0:
        break
    if sub < 0:
        head += 1
    else: rear -= 1

print(d[idx_1], end = " ")
print(d[idx_2])