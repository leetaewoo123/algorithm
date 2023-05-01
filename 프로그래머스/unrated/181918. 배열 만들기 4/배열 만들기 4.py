def solution(arr):
    stk = []
    for i in range (len(arr)):
        while i<len(arr):
            if len(stk)==0:
                stk.append(arr[i])
                break
            else:
                if stk[-1]<arr[i]:
                    stk.append(arr[i])
                    break
                else:
                    del stk[-1]
    return stk