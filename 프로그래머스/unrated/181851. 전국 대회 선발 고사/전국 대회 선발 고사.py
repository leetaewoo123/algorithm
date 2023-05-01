def solution(rank, attendance):
    answer = 0
    Trank = []
    for i in range (len(rank)):
        if attendance[i] == True:
            Trank.append(rank[i])
    Trank = sorted(Trank)
    return rank.index(Trank[0])*10000+rank.index(Trank[1])*100+rank.index(Trank[2])