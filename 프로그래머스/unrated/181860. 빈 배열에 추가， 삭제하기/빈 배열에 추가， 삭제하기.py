def solution(arr, flag):
    answer = ""
    for i in range (len(arr)):
        if flag[i] == True:
            answer += str(arr[i])*(arr[i]*2)
        else :
            answer = answer[:-arr[i]]
    return list(map(int,answer))