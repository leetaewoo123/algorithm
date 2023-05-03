def solution(score):
    answer = [0 for _ in range (len(score))]
    avg = []
    rank,n = 1,0
    for i in score:
        avg.append((i[0]+i[1])/2)
    avg_s = sorted(list(set(avg)),reverse=True)
    
    for i in avg_s:
        rank += n
        n = 0
        for j in range (len(avg)):
            if i == avg[j]:
                answer[j]= rank
                n += 1
    return answer