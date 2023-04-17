import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub(r"[^0-9a-z-_.]","",answer)
    
    answer = re.sub('(([.])\\2{1,})', '.', answer)
    
    if answer[0]=="." and answer[-1]==".":
        answer = answer[1:-1]
    elif answer[-1]==".":
        anaswer = answer[:-1]
    elif answer[0]==".":
        answer = answer[1:]
    
    if len(answer)==0:
        answer = "a"
        
    if len(answer)>= 16:
        answer = answer[:15]
    if answer[-1]==".":
        answer = answer[:-1]
        
    while len(answer)<3:
        answer+=answer[-1]
    return answer