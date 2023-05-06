def solution(s):
    answer = []
    cnt_zero,cnt  = 0,0
    while True:
        if s =="1":
            break
        cnt_zero += s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:]
        cnt += 1
    return [cnt,cnt_zero]