# Problem_90

import time
from itertools import combinations

start_time = time.time()

properties = set()

for i in combinations(range(10), 6):
    for j in combinations(range(10), 6):
        left = list(i)
        right = list(j)
        dice1 = ''.join(str(x) for x in left)
        dice2 = ''.join(str(x) for x in right)
        dice_set = tuple(sorted([dice1, dice2]))
        if 6 in left:
            left.append(9)
        if 9 in left:
            left.append(6)
        if 6 in right:
            right.append(9)
        if 9 in right:
            right.append(6)
        left = set(left)
        right = set(right)
        tmp = []
        for l in left:
            for r in right:
                tmp.extend([str(l)+str(r), str(r)+str(l)])
        chk_nums = ['01', '04', '09', '16', '25', '36', '49', '64', '81']
        for chk in chk_nums:
            if tmp.count(chk) == 0:
                break
        else:
            properties.add(dice_set)
print(len(properties))
print('%.6f seconds' % (time.time() - start_time))
