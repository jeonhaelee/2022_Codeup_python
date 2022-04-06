

d = []
numbers = []

n = int(input())
for i in range(n):
    c, no, name = input().split()
    no = int(no)
    data = (int(no), name)
    
    if c == 'I':
        if int(no) not in numbers:
            d.append(data)
            numbers.append(int(no))
            
    elif c == 'D':
        if no not in numbers:
            continue
        for i in d:
            if i[0] == no:
                find = i
        del d[d.index(find)]
        del numbers[numbers.index(no)]
            
d.sort(key = lambda x : x[0])

print_number = list(map(int, input().split()))
for i in print_number:
    print("{} {}".format(d[i-1][0],d[i-1][1]))