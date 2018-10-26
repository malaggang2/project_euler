# Problem_59
# XOR decryption
# Each character on a computer is assigned a unique code and the preferred standard
# is ASCII (American Standard Code for Information Interchange).
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII,
# then XOR each byte with a given value, taken from a secret key.
# The advantage with the XOR function is that using the same encryption key on
# the cipher text, restores the plain text;
# for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message,
# and the key is made up of random bytes.
# The user would keep the encrypted message and the encryption key in different locations,
# and without both "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method
# is to use a password as a key.
# If the password is shorter than the message, which is likely, the key is repeated
# cyclically throughout the message.
# The balance for this method is using a sufficiently long password key for security,
# but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower case characters.
# Using cipher.txt (right click and 'Save Link/Target As...'), a file containing
# the encrypted ASCII codes, and the knowledge that the plain text must contain
# common English words, decrypt the message and find the sum of the ASCII values
# in the original text.

import time
from itertools import permutations

start_time = time.time()
with open('problem_59.txt', 'r') as f:
    data = [int(c) for c in f.read().strip().split(',')]

for i in permutations([ord(c) for c in 'abcdefghijklmnopqrstuvwxyz'], 3):
    secret_key = list(i)
    new_data = []
    for index, coded_num in enumerate(data):
        decoded_num = coded_num ^ secret_key[index % 3]
        new_data.append(decoded_num)
    decrypted = ''.join([chr(n) for n in new_data])
    if 'the ' in decrypted:
        print(decrypted, '\n', sum(new_data))
        print("%.6f seconds" % (time.time() - start_time))
        break

import time
from collections import Counter

start_time = time.time()
with open('problem_59.txt', 'r') as f:
    data = [int(c) for c in f.read().strip().split(',')]

def get_secret_key(coded_data):
    freq = ord(' ')
    count = Counter()
    for index, coded_num in enumerate(coded_data):
        for key in 'abcdefghijklmnopqrstuvwxyz':
            if coded_num ^ ord(key) == freq:
                count.update([(ord(key), index % 3)])
                break
    return list(key for (key, index), frequency in sorted(count.most_common(3), key=lambda x:x[0][1]))

def decrypt(secret_key, coded_data):
    return [coded_num ^ secret_key[i % len(secret_key)] for i, coded_num in enumerate(coded_data)]

print(sum(decrypt(get_secret_key(data), data)))
print("%.6f seconds" % (time.time() - start_time))
