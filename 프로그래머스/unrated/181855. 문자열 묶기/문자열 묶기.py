def solution(strArr):
    answer = []
    cnt = []
    for i in strArr:
        cnt.append(len(i))
    for i in list(set(cnt)):
        answer.append(cnt.count(i))
    return max(answer)