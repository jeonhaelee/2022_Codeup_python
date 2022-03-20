arr = input()

# count_1 = 0; count_2 = 0
# for i in range(len(arr)):
#     if arr[i] == "(":
#         count_1 += 1
#     elif arr[i] == ")":
#         count_2 += 1
        
# print("{} {}".format(count_1, count_2))

print("{} {}".format(arr.count("("),arr.count(")")))
