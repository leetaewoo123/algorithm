def solution(want, number, discount):
    answer = 0
    dic = {}
    d_copy = dic.copy()
    for i in range (len(want)):
        dic[want[i]]= number[i]
        
    for i in range (len(discount)):
        d_copy = dic.copy()
        if i+10 > len(discount):
            return answer
        else:
            for j in range (i,i+10):
                if discount[j] in want:
                    d_copy[discount[j]] -= 1
            if all(x==0 for x in d_copy.values()) == True:
                answer += 1
    return answer