def solution(spell, dic):
    answer = 0
    
    for i in dic:
        word = 0
        for j in spell:
            if j in i:
                word += 1
            else:
                continue
        if word == len(spell):
            return 1
    
    return 2