def solution(my_string, s, e):
    if (s==0 and e ==0) or s==e:
        return my_string
    if s==0:
        return my_string[e::-1]+my_string[e+1:]
    return my_string[:s]+my_string[e:s-1:-1]+my_string[e+1:]
    