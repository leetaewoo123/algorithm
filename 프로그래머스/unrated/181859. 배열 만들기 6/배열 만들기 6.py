def solution(arr):
    stk = []
    for i in arr:
        if len(stk)==0 or i != stk[-1]:
            stk.append(i)
        else :
            del stk[-1]
    if len(stk)==0:
        return [-1]
    return stk