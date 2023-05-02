def solution(my_str, n):
    answer = []
    k = int(len(my_str)/n)
    my_str=list(my_str)
    for i in range (k):
        answer.append("".join(my_str[0:n]))
        del my_str[0:n]
    if len(my_str)>0:
        answer.append("".join(my_str))
    return answer