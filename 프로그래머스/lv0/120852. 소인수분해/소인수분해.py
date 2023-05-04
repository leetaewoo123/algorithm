def solution(n):
    answer = []
    cnt = 2
    while n != 1:
        if n%cnt == 0:
            n = n//cnt
            answer.append(cnt)
        else:
            cnt += 1
    return sorted(list(set(answer)))