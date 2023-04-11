def solution(a, b):
    answer = ''
    y = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    m = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    return y[(sum(m[:a-1])+b-1)%7]
     