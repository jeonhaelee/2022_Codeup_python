
n = int(input())
score = list(map(int,input().split()))
d = sorted(score, reverse=True)
rank = [1]

count = 0
for i in range(1, n):
    if d[i] < d[i-1]:
        rank.append(rank[i-1] + count + 1)
        count = 0
    elif d[i] == d[i-1]:
        rank.append(rank[i-1])
        count += 1
        
for i in range(n):
    print("{} {}".format(score[i], rank[d.index(score[i])]))