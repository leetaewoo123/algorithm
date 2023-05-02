def solution(bin1, bin2):
    answer = ''
    bin1,bin2 = bin1[::-1], bin2[::-1]
    k1, k2 = 0,0
    for i in range (len(bin1)):
        k1 += int(bin1[i])*(2**i)
    
    for i in range (len(bin2)):
        k2 += int(bin2[i])*(2**i)
    
    return format(k1+k2, 'b')