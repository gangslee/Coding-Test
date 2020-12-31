def solution(S):
    if 'XXX' in S and 'OOO' in S or not('XXX' in S or 'OOO' in S):
        return 'tie'
    elif 'XXX' in S:
        return 'X'
    elif 'OOO' in S:
        return 'O'
