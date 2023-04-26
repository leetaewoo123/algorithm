def solution(my_string):
    answer = ''
    r = []
    for i in my_string:
        if i not in r:
            r.append(i)
            answer += i
    return answer