
n = int(input())
m = int(input())

d = []
for i in range(m):
    a, b = map(int,input().split())
    d.append((a, b))

answer = []
for i in range(m):
    if d[i][0] == 1 or d[i][1] == 1:
        answer.append(d[i][0])
        answer.append(d[i][1])
answer = list(set(answer))
for j in range(n):
    for i in range(m):
        if d[i][0] in answer or d[i][1] in answer:
            answer.append(d[i][0])
            answer.append(d[i][1])
            answer = list(set(answer))
print(len(answer)-1)
