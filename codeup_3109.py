

def find_put_index(no,d):
    idx = 0
    if len(d) == 0:
        return idx
    if no < d[0][0]:
        return idx
    elif no > d[-1][0]:
        idx = len(d)
        return idx
    else :
        for i in range(len(d)-1):
            if d[i][0] < no and no < d[i+1][0]:
                idx = i+1
                return idx

def find_index(no, d):
    idx = 0
    for i in range(len(d)):
        if d[i][0] == no:
            idx = i
            return idx
            
d = []
numbers = []

n = int(input())

for i in range(n):
    c, no, name = input().split()
    no = int(no)
    data = (no, name)
    
    if c == 'I':
        if no not in numbers:
            d.insert(find_put_index(no,d), data)
            numbers.append(no)
        else:
            d.insert(find_index(no,d), data)
            numbers.append(no)
            
    elif c == 'D':
        if no not in numbers:
            continue
        for i in d:
            if i[0] == no:
                find = i
                break
        del d[d.index(find)]
        del numbers[numbers.index(no)]   


print_number = input().split()
for i in print_number:
    num = int(i)
    print("{} {}".format(d[num-1][0],d[num-1][1]))


