def solution(my_string, queries):
    answer = ''
    for i in queries:
        if i[0]==0:
            my_string = my_string[i[1]::-1]+my_string[i[1]+1:]
        else:
            my_string = my_string[:i[0]] + my_string[i[1]:i[0]-1:-1]+ my_string[i[1]+1:]
            
    return my_string