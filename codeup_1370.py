

h, r = map(int, input().split())

star = "*"
space = " "

cnt = h*2-1

for j in range(r):
    answer = ""
    for i in range(h):
        answer = space*i
        print(answer+star)
            
    for i in range(h-2, -1, -1):
        answer = space*i
        print(answer+star)
