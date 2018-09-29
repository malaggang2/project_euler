# Problem_24
# Lexicographic permutations
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the
# digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#
from math import factorial

source = [i for i in range(10)]     # 주어진 숫자 0 ~ 9
order = 0                           # 숫자를 조합하여 만들었을 때 해당 숫자의 순서
answer = ''
for num in range(9, -1, -1):
    for digit in range(1, 10):
        if order + (digit * factorial(num)) >= 1000000:
            answer += str(source.pop(digit - 1))
            break
    order += factorial(num) * (digit - 1)
print(answer)

# # 내장모듈 활용
# from itertools import permutations
# nums = permutations('0123456789')
# print(''.join(list(nums)[1000000-1]))
