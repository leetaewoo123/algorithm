def solution(arr, queries):
    answer = []
    for i in queries:
        n = []
        for j in arr[i[0]:i[1]+1]:
            if j > i[2]:
                n.append(j)
                
        if len(n)==0:
            answer.append(-1)
        else:
            answer.append(min(n))
    return answer