def solution(s):
    answer = []
    s= list(s)
    n=[]
    for i in range (len(s)):
        for j in range (i+1):
            if s[i]==s[j]:
                n.append(j)
        
        if len(n)==1:
            answer.append(-1)
        else : 
            answer.append(n[-1]-n[-2])
        n=[]

    return answer