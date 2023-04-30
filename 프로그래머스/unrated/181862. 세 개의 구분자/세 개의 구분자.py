def solution(myStr):
    answer = []
    myStr = myStr.replace("a","@").replace('b',"@").replace('c',"@")
    for i in myStr.split('@'):
        if i != "":
            answer.append(i)
    if len(answer) == 0:
        return ["EMPTY"]
    return answer