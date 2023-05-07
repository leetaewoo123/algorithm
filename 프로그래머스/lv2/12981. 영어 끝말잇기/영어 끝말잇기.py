def solution(n, words):
    answer = [words[0]]
    
    for i in range (1,len(words)):
        if (answer[-1][-1]!=words[i][0]) or (words[i] in answer):
            k=i
            if (k+1)%n ==0:
                num = n
            else :
                num = (k+1)%n
            return [num, (k)//n+1]
        else:
            answer.append(words[i])
    return [0,0]