def solution(my_string):
    answer = 0
    n = "0"
    for i in range (len(my_string)):
        if my_string[i].isdigit():
            n += str(my_string[i])
        else:
            answer += int(n)
            n = "0"
    if n != "0":
        answer += int(n)
    return answer