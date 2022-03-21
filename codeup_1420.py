n = int(input())
d = []
for i in range(n):
    d.append(input().split())
    
dic = {}

for i in range(n):
    dic[d[i][0]] = d[i][1]

        
print(dic)