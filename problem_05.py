# Problem_05
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import time

def is_prime_num(n):
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def smallest_multiple(n):
    smallest_multiple_num = 1

    # 입력값 이하의 소인수 리스트를 만듦
    prime_list = []
    for num in range(2, n + 1):
        if is_prime_num(num):
            prime_list.append(num)

    # 입력값 이하인 소인수의 최대 제곱수를 dict로 반환
    prime_factor_dict = {}
    for prime in prime_list:
        i = 1
        while prime**i <= n:
            i += 1
        prime_factor_dict[prime] = i - 1

    for key in prime_factor_dict.keys():
        smallest_multiple_num *= key**prime_factor_dict[key]
    return(smallest_multiple_num)

start_time = time.time()
print(smallest_multiple(20))
print("%f seconds" % (time.time() - start_time))


# # what a genius!
# gcd = 1
# for i in range(2, 21):
#     x = gcd
#     while gcd % i != 0:
#         gcd += x
# print(gcd)
