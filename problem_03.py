# Problem_03
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

n = 600851475143
i = 2
ans = 2

while n != 1:
    if n % i == 0:
        n = n // i
        if i > ans:
            ans = i
    else:
        i += 1
print(ans)

# def get_max_prime_number(n):
#     i = 2
#     max_prime_number = 2
#     while n != 1:
#         if n % i == 0:
#             n = n // i
#             if i > max_prime_number:
#                 max_prime_number = i
#         else:
#             i += 1
#     return max_prime_number
# print(get_max_prime_number(600851475143))


# function to check prime number
#
# def is_prime_number(n):
#     for i in range(2, int(n**0.5 + 1)):
#         if n % i == 0:
#             return False
#     return True
#
# print(is_prime_number(29))
