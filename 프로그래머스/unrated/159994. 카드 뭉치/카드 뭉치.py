def solution(cards1, cards2, goal):
    result = 'Yes'
    cards1_idx = cards2_idx = 0
    for i in (goal):
        if len(cards1)> cards1_idx and i==cards1[cards1_idx]:
            cards1_idx += 1
        elif len(cards2) > cards2_idx and i==cards2[cards2_idx]:
            cards2_idx += 1
        else : result = 'No'
    return result