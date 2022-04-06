

d = []
b_scores = []
c_scores = []

n = int(input())

for i in range(n):
    name, a, b, c = input().split()
    d.append({'name':name, 'a':int(a), 'b':int(b), 'c':int(c)})
    b_scores.append(int(b))
    c_scores.append(int(c))

d.sort(key = lambda x : -x['a'])
name_1st = d[0]

b_scores.sort(reverse=True)
c_scores.sort(reverse=True)

b_rank = b_scores.index(name_1st['b'])+1
c_rank = c_scores.index(name_1st['c'])+1

print("{} {} {}".format(name_1st['name'], b_rank, c_rank))