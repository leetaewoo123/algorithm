def solution(survey, choices):
    answer = ''
    dic = {'R' : 0, 'T' : 0, 'C' : 0, 'F': 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    j = 0
    for i in survey:
        if choices[j]>4:
            dic[i[1]] += choices[j]-4
            j+= 1
        elif choices[j]==4:
            j+=1
        else : 
            dic[i[0]] += 4-choices[j]
            j+= 1
    
    if dic.get("R") >= dic.get('T'):
        answer += "R"
    else :
        answer += "T"
        
    if dic.get('C') >= dic.get('F'):
        answer += "C"
    else :
        answer += "F"
        
    if dic.get('J') >= dic.get('M'):
        answer += "J"
    else :
        answer += "M"
        
    if dic.get('A') >= dic.get('N'):
        answer += "A"
    else :
        answer += "N"
        
    

    return answer