def solution(picture, k):
    answer = []
    for i in picture:
        n = ''
        for j in range (len(i)):
            n += i[j]*k
        for z in range (k):
            answer.append(n)
    return answer