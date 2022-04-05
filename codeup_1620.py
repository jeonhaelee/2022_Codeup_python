
import numpy as np

def str_sum(str_num):
    sum = 0
    sum = np.array(list(map(lambda x : int(str_num[x]), range(len(str_num)))))
    return np.sum(sum)
    
def sum_one(num):
    while num // 10 != 0:
        num = str_sum(str(num))
    return print(num)

sum_one(int(input()))

