
class stack:
    def __init__(self):
        self.d = []
    def push(self, num):
        self.d.append(num)
    def top(self):
        if len(self.d) == 0:
            print(-1)
        else: print(self.d[-1])
    def pop(self):
        del self.d[-1]
    def size(self):
        print(len(self.d))
    def empty(self):
        if len(self.d) == 0:
            print('true')
        else: print('false')

stack1 = stack()
n = int(input())
for i in range(n):
    command = input()
    if command[:4] == 'push':
        num = int(command[6])
        stack1.push(num)
    elif command[:3] == 'top':
        stack1.top()
    elif command[:3] == 'pop':
        stack1.pop()
    elif command[:4] == 'size':
        stack1.size()
    elif command[:5] == 'empty':
        stack1.empty()
