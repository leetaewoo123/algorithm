def solution(array, commands):
    answer = []
    for i in commands:
        ary = sorted(array[i[0]-1:i[1]])
        answer.append(ary[i[2]-1])
    return answer