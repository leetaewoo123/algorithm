def solution(t, p):
    answer = 0
    num =[]
    m=0
    for i in range (len(p), len(t)+1):
        num.append(t[m:i])
        m+=1
    for i in range(len(num)):
        if int(num[i])<=int(p):
            answer +=1
    return answer