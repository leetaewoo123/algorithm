def solution(emergency):
    answer = []
    rank = emergency
    rank = sorted(rank,reverse = True)
    for i in emergency:
        for j in rank:
            if i == j :
                answer.append(rank.index(i)+1)
    return answer