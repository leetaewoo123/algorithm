def solution(arr):
    answer = [2]
    if 2 not in arr:
        return [-1]
    elif arr.count(2)==1:
        return [2]
    else:
        for i in range (arr.index(2)+1,len(arr)):
            if arr[i]==2 and 2 not in (arr[i+1:]):
                answer.append(arr[i])
                break
            else:
                answer.append(arr[i])
    return answer