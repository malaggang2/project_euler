# Problem_42
# Coded triangle numbers
# The nth term of the sequence of triangle numbers is given by,
# tn = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to
# its alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common English words,
# how many are triangle words?

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
TRIANGLE_NUMBERS = list(map(lambda x:x*(x+1)/2, [n for n in range(1, 26)]))

with open('problem_42.txt', 'r') as f:
    source = [word for word in f.read().strip().replace('"', '').split(",")]

answer = 0
for word in source:
    value = 0
    for alphabet in word:
        value += ALPHABET.index(alphabet) + 1
    if value in TRIANGLE_NUMBERS:
        answer += 1
print(answer)
