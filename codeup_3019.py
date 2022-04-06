

d = []
n = int(input())

for i in range(n):
    work, year, month, day = input().split()
    d.append({'work':work, 'year':int(year), 'month':int(month), 'day':int(day)})
    
d.sort(key=lambda x : (x['year'], x['month'], x['day'], x['work']))

for i in d:
    print(i['work'])