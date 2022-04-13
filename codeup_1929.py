

class Ques():
    def __init__(self, n):
        self.n = n
        self.d = [n]
        
    def f(self):
        if self.n == 1:
            return 0
        if self.n % 2 == 0:
            self.n = self.n/2
            self.d.append(int(self.n))
            self.f()
        else: 
            self.n = (3*self.n)+1
            self.d.append(int(self.n))
            self.f()

def get_list(result, idx):
    if idx >= 0:
        print(result[idx])
        idx -= 1
        get_list(result, idx)
    else: return 0
    
n = int(input())

ques = Ques(n)
ques.f()
result = ques.d

idx = len(result) - 1
get_list(result, idx)