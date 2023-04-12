def solution(name, yearning, photo):
    answer = []
    
    for i in range (len(photo)):
        cnt = 0
        for j in range (len(photo[i])):
            if (photo[i][j]) in name :
                a = name.index(photo[i][j])
                cnt+= yearning[a]
            else : 
                cnt += 0
        answer.append(cnt)
    return answer