# Problem_89
# Roman numerals
import time
from collections import Counter

start_time = time.time()

denominations = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000,
    '0': 4, '1': 9, '2':40, '3': 90, '4': 400, '5': 900
    }
subtractives = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

with open('problem_89.txt', 'r') as f:
    data = [n for n in f.read().strip().split('\n')]

answer = 0
for i in data:
    decoded_num = 0
    r_num = i
    for j, s in enumerate(subtractives):
        if s in r_num:
            tmp = r_num.replace(s, str(j))
            r_num = tmp
    for r, c in Counter(r_num).items():
        decoded_num += denominations[r] * c

    encoded = ''
    digits = [n for n in range(len(str(decoded_num)))][::-1]
    for n, d in zip(str(decoded_num), digits):
        n = int(n)
        if d == 3:
            encoded += 'M' * n
        if d == 2:
            if n == 9:
                encoded += 'CM'
            elif n >= 5:
                encoded += 'D' + 'C' * (n - 5)
            elif n == 4:
                encoded += 'CD'
            else:
                encoded += 'C' * n
        if d == 1:
            if n == 9:
                encoded += 'XC'
            elif n >= 5:
                encoded += 'L' + 'X' * (n - 5)
            elif n == 4:
                encoded += 'XL'
            else:
                encoded += 'X' * n
        if d == 0:
            if n == 9:
                encoded += 'IX'
            elif n >= 5:
                encoded += 'X' + 'I' * (n - 5)
            elif n == 4:
                encoded += 'IX'
            else:
                encoded += 'I' * n
    answer += len(i) - len(encoded)

print(answer)
print('%.6f seconds' % (time.time() - start_time))

# import time
# start_time = time.time()
#
# substitutions = [("VIIII", "IX"), ("IIII", "IV"), ("LXXXX", "XC"), ("XXXX", "XL"), ("DCCCC", "CM"), ("CCCC", "CD")]
#
# with open("problem_89.txt", 'r') as f:
#     data = f.read().strip()
#
# len_orign = len(data)
# for prev, after in substitutions:
#     tmp = data.replace(prev, after)
#     data = tmp
#
# len_after = len(data)
#
# print(len_orign - len_after)
# print('%.6f seconds' % (time.time() - start_time))
