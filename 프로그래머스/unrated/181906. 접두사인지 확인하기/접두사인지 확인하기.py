def solution(my_string, is_prefix):
    answer = 0
    str1 = ""
    for i in my_string:
        str1 += i
        if str1 == is_prefix:
            return 1
    
    return answer