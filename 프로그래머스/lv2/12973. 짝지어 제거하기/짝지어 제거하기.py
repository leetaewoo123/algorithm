def solution(s):
    word = []
    
    for i in range (len(s)):
        if not word:
            word.append(s[i])
        else:
            if s[i]==word[-1]:
                word.pop()
            else:
                word.append(s[i])
    if word:
        return 0
    else:
        return 1