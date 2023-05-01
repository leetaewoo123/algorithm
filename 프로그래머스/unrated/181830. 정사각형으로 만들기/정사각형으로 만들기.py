def solution(arr):
    if len(arr) == len(arr[0]):
        return arr
    else :
        if len(arr) > len(arr[0]):
            n = len(arr[0])-len(arr)
            for i in range (len(arr)):
                arr[i].extend([0]*(len(arr)-len(arr[i])))
            return arr
        else:
            for i in range (len(arr[0])-len(arr)):
                arr.append([0]*len(arr[0]))
            return arr