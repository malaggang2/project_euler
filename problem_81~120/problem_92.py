# Problem_92
# Square digit chains
import time
from itertools import permutations

start_time = time.time()

squares = [n**2 for n in range(10)]

limit = 10**7
set1 = set()
set2 = set()
answer = 0
for i in range(1, limit):
    chk = i
    chains = []
    while True:
        tmp = 0
        for j in str(chk):
            tmp += squares[int(j)]
        if tmp in set1:
            set1.update(chains)
            break
        if tmp in set2:
            set2.update(chains)
            answer += 1
            break
        if tmp in chains:
            break
        chains.extend([tmp] + [int(''.join(i)) for i in permutations(str(tmp))])
        chk = tmp
    if 1 in chains:
        set1.update(chains)
    if 89 in chains:
        set2.update(chains)
        answer += 1
print(answer)
print('%.6f seconds' % (time.time() - start_time))
