# Problem_93
# Arithmetic expressions

import time
from itertools import permutations, product, combinations

start_time = time.time()

operations = ['+', '-', '*', '/']

max_length = 0
answer = None
for num in combinations(range(1, 10), 4):
    result_nums = set()
    for i in permutations(num):
        for j in product(operations, repeat=3):
            i = [str(n) for n in i]
            tmp = []
            for p in zip(i, j):
                tmp.extend([n for n in p])
            tmp.append(i[3])
            num_operations = ''.join(tmp)
            n1 = num_operations
            n2 = '({}){}'.format(num_operations[:3], num_operations[3:])
            n3 = '({}){}({})'.format(num_operations[:3], num_operations[3], num_operations[4:])
            n4 = '{}({}){}'.format(num_operations[:2], num_operations[2:5], num_operations[5:])
            n5 = '{}({})'.format(num_operations[:4], num_operations[4:])
            n6 = '(({}){}){}'.format(num_operations[:3], num_operations[3:5], num_operations[5:])
            n7 = '({}({})){}'.format(num_operations[:2], num_operations[2:5], num_operations[5:])
            n8 = '({}){}'.format(num_operations[:5], num_operations[5:])
            n9 = '{}({})'.format(num_operations[:2], num_operations[2:])
            n10 = '{}(({}){})'.format(num_operations[:2], num_operations[2:5], num_operations[5:])
            n11 = '{}({}({}))'.format(num_operations[:2], num_operations[2:4], num_operations[4:])
            tmp_expressions = (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11)
            for exp in tmp_expressions:
                try:
                    if eval(exp) == int(eval(exp)) and int(eval(exp)) > 0:
                        result_nums.add(int(eval(exp)))
                except ZeroDivisionError:
                    pass
            for chk in range(1, len(result_nums)+1):
                if list(result_nums).count(chk) != 1:
                    chk_length = chk - 1
                    break
            if chk_length > max_length:
                max_length = chk_length
                answer = num
print(''.join(str(n) for n in answer), max_length)
print('%.6f seconds' % (time.time() - start_time))
