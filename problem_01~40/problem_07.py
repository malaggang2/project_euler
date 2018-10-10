# Problem_07
# 10001st prime
import time

def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True

prime_list = []
num = 2
start_time = time.time()
while len(prime_list) != 10001:
    if is_prime(num):
        prime_list.append(num)
    num += 1
print(prime_list[-1])
print("%f seconds" % (time.time() - start_time))

#
# prime_list2 = [2]
# num2 = 3
# start_time2 = time.time()
# while len(prime_list2) != 10001:
#     if is_prime(num2):
#         prime_list2.append(num2)
#     num2 += 2
#
# print(prime_list2[-1])
# print("%f seconds" % (time.time() - start_time2))
