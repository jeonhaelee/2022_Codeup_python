
n = int(input())
d = list(map(int,input().split()))

m = int(input())
q = input()

num = ""
for i in range(len(q)):
    if q[i] == " ":
        if int(num) in d:
            print(1, end = " ")
        else : print(0, end = " ")
        num = ""
        continue
    num += q[i]
if int(num) in d:
    print(1, end = " ")
else : print(0, end = " ")
    

   


        