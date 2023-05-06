def solution(s):
    answer = True
    cnt_r, cnt_l = 0,0
    for i in range (len(s)):
        if s[0]==")":
            return False
        if s[i]=="(":
            cnt_r += 1
        elif cnt_r > cnt_l and s[i]==")":
            cnt_l += 1

    if cnt_r == cnt_l:
        return True
    else:
        return False