# Problem_79
# Passcode derivation
# A common security method used for online banking is to ask the user for three
# random characters from a passcode. For example, if the passcode was 531278,
# they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
# The text file, keylog.txt, contains fifty successful login attempts.
# Given that the three characters are always asked for in order, analyse the file
# so as to determine the shortest possible secret passcode of unknown length.

import time

start_time = time.time()

with open('problem_79.txt', 'r') as f:
    data = [n for n in f.read().strip().split('\n')]

order_info = dict()
for n in data:
    for i in range(3):
        if n[i] in order_info:
            order_info[n[i]].update([x for x in n[:i]])
        else:
            order_info[n[i]] = set()
            order_info[n[i]].update([x for x in n[:1]])

order_count = [[n, len(info)] for n, info in order_info.items()]
print(''.join([n for n, _ in sorted(order_count, key=lambda x:x[1])]))
print("%.6f seconds" % (time.time() - start_time))
