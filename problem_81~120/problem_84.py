# Problem_84
# Monopoly odds
import time
from random import randint, shuffle

start_time = time.time()

source = 'GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL C1 U1 C2 C3 R2 D1 CC2 D2 D3 FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 G2J G1 G2 CC3 G3 R4 CH3 H1 T2 H2'
board = [s for s in source.strip().split(' ')]
cc_card = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'GO', 'JAIL']
ch_card = ['X', 'X', 'X', 'X', 'GO', 'C1', 'E3', 'H2', 'R1', 'RN', 'RN', 'UN', 'B3']
railways = [board.index('R1'), board.index('R2'), board.index('R3'), board.index('R4')]
utilities = [board.index('U1'), board.index('U2')]

shuffle(cc_card)
shuffle(ch_card)
cc_card_pick = 0
ch_card_pick = 0
square_visit = {pos:0 for pos, _ in enumerate(board)}
double_count = 0
position = 0
for i in range(10**5):
    cc_card_get = None
    ch_card_get = None
    dice1, dice2 = randint(1, 4), randint(1, 4)
    position += (dice1 + dice2)
    position %= 40
    if dice1 == dice2:
        double_count += 1
    else:
        double_count = 0
    if double_count == 3:
        double_count = 0
        position = board.index('JAIL')
        square_visit[position] += 1
    if board[position] in ['CH1', 'CH2', 'CH3']:
        ch_card_get = ch_card[ch_card_pick]
        ch_card_pick = (ch_card_pick + 1) % len(ch_card)
        if ch_card_get in ['GO', 'C1', 'E3', 'H2']:
            position = board.index(ch_card_get)
            square_visit[position] += 1
        elif ch_card_get == 'R1':
            position = board.index(ch_card_get)
            square_visit[position] += 1
        elif ch_card_get == 'RN':
            if board[position] == 'CH3':
                position = board.index('R1')
                square_visit[position] += 1
            else:
                position = min([n for n in railways if n > position])
                square_visit[position] += 1
        elif ch_card_get == 'UN':
            if board[position] == 'CH3':
                position = board.index('U1')
                square_visit[position] += 1
            else:
                position = min([n for n in utilities if n > position])
                square_visit[position] += 1
        elif ch_card_get == 'B3':
            position -= 3
            if position < 0:
                position += 40
            square_visit[position] += 1
        else:
            square_visit[position] += 1
    elif board[position] in ['CC1', 'CC2', 'CC3']:
        cc_card_get = cc_card[cc_card_pick]
        cc_card_pick = (cc_card_pick + 1) % len(cc_card)
        if cc_card_get == 'GO':
            position = 0
            square_visit[position] += 1
        elif cc_card_get == 'JAIL':
            position = board.index(cc_card_get)
            square_visit[position] += 1
        else:
            square_visit[position] += 1
    elif position == board.index('G2J'):
        position = board.index('JAIL')
        square_visit[position] += 1
    else:
        square_visit[position] += 1

print(''.join([str(n) for n, _ in sorted(square_visit.items(), key=lambda x: x[1], reverse=True)[:3]]))
print('%.6f seconds' % (time.time() - start_time))
