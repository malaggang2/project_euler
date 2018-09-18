# Problem_14
# Longest Collatz sequence

# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# Once the chain starts the terms are allowed to go above one million.
import time

def collatz(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = 3 * num + 1
        count += 1
    return count

start_time = time.time()

longest_collatz = 0
for i in range(1, 1000001, 2):
    if collatz(i) > longest_collatz:
        longest_collatz = collatz(i)
        max_num = i
print(max_num, longest_collatz)
print("%.6f seconds" % (time.time() - start_time))

# dict type을 활용하여, 확인하는 과정에서 이미 한 번 사용했던 숫자는 dict에 저장하여 캐쉬 역할을 하게 하면 시간을 획기적으로 줄일 수 있음.
# 공부해봐야 할 주제
#
# class Hailstone:
#
#     def __init__(self):
#         self.store = {1: 1}
#
#     def __call__(self, n):
#         chk = 0
#         original = n
#
#         while n >= 1:    # n 이 0 일 경우를 생각해서
#             if n in self.store:
#                 self.store[original] = self.store[n] + chk
#                 return self.store[n] + chk
#
#             if n%2 == 0:
#                 n = n // 2
#             else:
#                 n = 3 * n + 1
#
#             chk += 1
#
#         self.store[original] = chk
#         return chk
#
# start_time = time.time()
# h = Hailstone()
#
# for n in range(10**6+1):
#     h(n)
# print(max(h.store, key=lambda k: h.store[k]))
# print("{}".format(time.time() - start_time))
