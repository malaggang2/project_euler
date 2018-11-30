# Problem_95
# Amicable Chains

import time

start_time = time.time()

nums = [0 for n in range(10**6)]
for i in range(1, len(nums)):
    for j in range(i*2, len(nums), i):
        nums[j] += i

max_length = 0
for i in range(2, 10**6):
    chains = [i]
    num = i
    while True:
        chk_num = nums[num]
        if chk_num == i or chk_num in chains or chk_num > 10**6:
            break
        chains.append(chk_num)
        num = chk_num
    if chk_num == i:
        chk_length = len(chains)
        if chk_length > max_length:
            max_length = chk_length
            answer = min(chains)
print(answer)
print('%.6f seconds' % (time.time() - start_time))
