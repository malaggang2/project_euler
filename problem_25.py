# Problem 25
# 1000-digit Fibonacci number
# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

prev, after = 1, 1
count = 2
while len(str(after)) < 1000:
    prev, after = after, prev + after
    count += 1
print(count)
