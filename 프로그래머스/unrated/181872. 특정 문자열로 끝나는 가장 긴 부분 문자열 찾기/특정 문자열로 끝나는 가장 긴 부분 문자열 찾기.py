def solution(myString, pat):
    answer = ''
    word = ""
    for i in range (len(myString)-1,-1,-1):
        word = myString[i]+word
        if pat in word:
            if i == len(myString)-1:
                return myString
            else:
                return myString[:i]+pat