def solution(quiz):
    z=[]
    for i in quiz:
        a,b = 0,0
        i = i.split(" ")
        if i[1]=="-":
            if int(i[0])-int(i[2])== int(i[-1]):
                z.append("O")
            else : z.append("X")
        else :
            if int(i[0])+int(i[2])== int(i[-1]):
                z.append("O")
            else : z.append("X")
                
    return z