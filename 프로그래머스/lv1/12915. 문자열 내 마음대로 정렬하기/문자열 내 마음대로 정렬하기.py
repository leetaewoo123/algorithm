def solution(strings, n):
    answer = []
    word = []
    for i in range (len(strings)):
        answer.append([strings[i][n],strings[i]])
    
    answer.sort()
    for i in range (len(strings)):
        word.append(answer[i][1])
    return word