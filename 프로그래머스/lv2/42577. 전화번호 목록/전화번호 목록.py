def solution(phone_book):
    answer = True
    ph = sorted(phone_book)
    for i in range (len(ph)-1):
        for j in range (len(ph[i+1])):
            if ph[i] == ph[i+1][:j]:
                return False
    return answer