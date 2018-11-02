# Problem_68
# Magic 5-gon ring
# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
# and each line adding to nine.
# Working clockwise, and starting from the group of three with the numerically
# lowest external node (4,3,2 in this example), each solution can be described uniquely.
# For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.
# It is possible to complete the ring with four different totals: 9, 10, 11, and 12.
# There are eight solutions in total.
# By concatenating each group it is possible to form 9-digit strings; the maximum
# string for a 3-gon ring is 432621513.
# Using the numbers 1 to 10, and depending on arrangements, it is possible to
# form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic"
# 5-gon ring?

import time
from itertools import permutations

start_time = time.time()

result = set()
externals = (3, 5, 7, 9)
internals = (1, 2, 4, 6, 8, 10)
for i in permutations([n for n in range(1, 11) if n != 6]):
    chk_list = [6, *i]
    chk_list.append(chk_list[1])
    flag1, flag2 = False, False
    for inter in internals:
        if chk_list[inter] == 10:
            flag1 = True
            break
    for ex in externals:
        if chk_list[ex] not in [7, 8, 9, 10]:
            flag2 = True
            break
    if flag1 or flag2:
        continue
    if sum(chk_list[:3]) == 14:
        tmp = [''.join(map(str, chk_list[:3]))]
        for j in range(2, 9, 2):
            chk_num = [chk_list[j+1], chk_list[j], chk_list[j+2]]
            if sum(chk_num) != 14:
                break
            else:
                tmp.append(''.join(map(str, chk_num)))
        else:
            result.add(int(''.join(tmp)))
print(max(result))
print("%.6f seconds" % (time.time() - start_time))

# import time
# from itertools import permutations
# start_time = time.time()
# lines = ((0, 5, 6), (1, 6, 7), (2, 7, 8), (3, 8, 9), (4, 9, 5))
# result = set()
# for ext in permutations(range(7, 11)):
#     for inter in permutations(range(1, 6)):
#         numbers = (6, *ext, *inter)
#         tmp = []
#         for line in lines:
#             chk_num = [numbers[x] for x in line]
#             if sum(chk_num) != 14:
#                 break
#             else:
#                 tmp.append(''.join(str(n) for n in chk_num))
#         else:
#             result.add(''.join(tmp))
# print(max(int(x) for x in result))
# print("%.6f seconds" % (time.time() - start_time))
