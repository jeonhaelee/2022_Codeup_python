
n = int(input())
number = input()


num = number[::-1]
answer = ""
for i in range(n):
    answer += num[i]
    if i != n-1:
        if (i+1) % 3 == 0:
            answer += ','
print(answer[::-1])