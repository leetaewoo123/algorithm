def solution(code):
    answer = ''
    mode = "0"
    for i in range (len(code)):
        if code[i]=="1":
            if mode == '0':
                mode = "1"
                continue
            elif mode == '1': 
                mode = "0"
                continue
        if mode == "0" and i % 2 == 0:
            answer += code[i]
        if mode == "1" and i % 2 != 0:
            answer += code[i]
    if len(answer)==0:
        return "EMPTY"
    return answer