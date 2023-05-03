def solution(A, B):
    answer = 0
    newlist = list(A)+[""]
    if A==B:
        return answer
    else :
        for _ in range (len(A)):
            A = A[-1]+A[:-1]
            answer += 1
            if A==B:
                return answer
                
        return -1
