def solution(my_string):
    answer,UP,LOW = [],[],[]
    for i in range (26):
        UP.append(chr(65+i))
        LOW.append(chr(97+i))
    word = UP+LOW
    word_dic = {key: 0 for key in dict.fromkeys(word).keys()}
    
    for i in range (len(my_string)):
        word_dic[my_string[i]] += 1
        
    for i in word_dic.values():
        answer.append(i)
    return answer