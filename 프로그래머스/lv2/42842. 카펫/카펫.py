def solution(brown, yellow):
    answer = []
    k = brown + yellow
    for i in range (1,yellow+1):
        if yellow%i==0 and (i+2)*((yellow//i)+2)==k:
            return [yellow//i+2,i+2]
    return answer