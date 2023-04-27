def solution(lines):
    answer = 0
    a = set([i for i in range (lines[0][0],lines[0][1])])
    b = set([i for i in range (lines[1][0],lines[1][1])])
    c = set([i for i in range (lines[2][0],lines[2][1])])
    
    
    return len(list((a&c) | (a&b) | (b&c)))