# Problem_54
# Poker hands
# In the card game poker, a hand consists of five cards and are ranked,
# from lowest to highest, in the following way:
#
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the highest value wins;
# for example, a pair of eights beats a pair of fives (see example 1 below).
# But if two ranks tie, for example, both players have a pair of queens,
# then highest cards in each hand are compared (see example 4 below);
# if the highest cards tie then the next highest cards are compared, and so on.
#
# The file, poker.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space):
# the first five are Player 1's cards and the last five are Player 2's cards.
# You can assume that all hands are valid (no invalid characters or repeated cards),
# each player's hand is in no specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?

import time

start_time = time.time()
with open('problem_54.txt', 'r') as f:
    data = [i.split(' ') for i in f.read().strip().split('\n')]

SUITS = 'SDHC'
VALUES = {char: score for score, char in enumerate('23456789TJQKA', 2)}
RANKS = {'royalstraightflush': 10, 'straightflush': 9, 'four_of_a_kind': 8,
    'full_house': 7, 'flush': 6, 'straight': 5, 'three_of_a_kind' : 4, 'two_pairs' : 3,
    'onepair' : 2, 'high_card' : 1
    }

def get_rank(a):
    pairs = 0
    consists = ''
    three_of_a_kind = False
    four_of_a_kind = False
    num_of_suits = 0
    for value in '23456789TJQKA':
        if a[:5].count(value) == 2:
            pairs += 1
            consists += value
        elif a[:5].count(value) == 3:
            three_of_a_kind = True
            consists = value
        elif a[:5].count(value) == 4:
            four_of_a_kind = True
            consists = value
    if max([a.count(char) for char in SUITS]) == 5:
        if a[:5] == 'TJQKA':
            rank = 'royalstraightflush'
        elif a[:5] in '23456789TJQK':
            rank = 'straightflush'
        elif four_of_a_kind:
            rank = 'four_of_a_kind'
        elif three_of_a_kind and pairs == 1:
            rank = 'full_house'
        else:
            rank = 'flush'
    else:
        if four_of_a_kind:
            rank = 'four_of_a_kind'
        elif three_of_a_kind and pairs == 1:
            rank = 'full_house'
        elif a[:5] in 'A23456789TJQKA':
            rank = 'straight'
        elif three_of_a_kind:
            rank = 'three_of_a_kind'
        elif pairs == 2:
            rank = 'two_pairs'
        elif pairs == 1:
            rank = 'onepair'
        else:
            rank = 'high_card'
    return consists, rank

win = 0
for i in data:
    player1 = ''.join(i[0] for i in sorted(i[:5]) if i[0] in '23456789') \
        + ''.join(sorted([i[0] for i in sorted(i[:5]) if i[0] in 'TJQKA'], key=lambda char: VALUES[char]))
    player2 = ''.join(i[0] for i in sorted(i[5:]) if i[0] in '23456789') \
        + ''.join(sorted([i[0] for i in sorted(i[5:]) if i[0] in 'TJQKA'], key=lambda char: VALUES[char]))
    consist1, rank1 = get_rank(player1)
    consist2, rank2 = get_rank(player2)
    if RANKS[rank1] > RANKS[rank2]:
        win += 1
    elif RANKS[rank1] == RANKS[rank2]:
        if rank1 in ['high_card', 'straight', 'flush', 'straightflush', 'royalstraightflush']:
            compare1 = sorted([VALUES[i] for i in player1[:5]])[::-1]
            compare2 = sorted([VALUES[i] for i in player2[:5]])[::-1]
            for p1, p2 in zip(compare1, compare2):
                if p1 > p2:
                    win += 1
                    break
                elif p1 < p2:
                    break
                else:
                    pass
        elif rank1 in ['onepair', 'three_of_a_kind', 'full_house', 'four_of_a_kind']:
            if VALUES[consist1] > VALUES[consist2]:
                win += 1
            elif VALUES[consist1] == VALUES[consist2]:
                remain1 = ''.join([i for i in list(player1[:5]) if i != consist1][::-1])
                remain2 = ''.join([i for i in list(player2[:5]) if i != consist2][::-1])
                for p1, p2 in zip(remain1, remain2):
                    if VALUES[p1] > VALUES[p2]:
                        win +=1
                        break
                    elif VALUES[p1] < VALUES[p2]:
                        break
                    else:
                        pass
        elif rank1 == 'two_pairs':
            if max(VALUES[consist] for consist in consist1) > max(VALUES[consist] for consist in consist2):
                win += 1
            elif max(VALUES[consist] for consist in consist1) == max(VALUES[consist] for consist in consist2):
                if min(VALUES[consist] for consist in consist1) > min(VALUES[consist] for consist in consist2):
                    win += 1
                if min(VALUES[consist] for consist in consist1) == min(VALUES[consist] for consist in consist2):
                    remain1 = ''.join([i for i in list(player1[:5]) if i not in consist1][::-1])
                    remain2 = ''.join([i for i in list(player2[:5]) if i not in consist2][::-1])
                    for p1, p2 in zip(remain1, remain2):
                        if VALUES[p1] > VALUES[p2]:
                            win +=1
                            break
                        elif VALUES[p1] < VALUES[p2]:
                            break
                        else:
                            pass
print(win)
print('%.6f seconds' % (time.time() - start_time))
