# Problem_04
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import time

def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

start_time = time.time()
largest_palindrome = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        check_num = i * j
        if is_palindrome(str(check_num)) and check_num > largest_palindrome:
            largest_palindrome = check_num

print(largest_palindrome)
print("{} seconds".format(time.time() - start_time))
