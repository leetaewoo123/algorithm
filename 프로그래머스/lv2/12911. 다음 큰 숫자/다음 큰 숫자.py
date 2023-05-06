def solution(n):
    k = n+1
    while True:
        if str(bin(n)[2:]).count("1") == str(bin(k)[2:]).count("1"):
            return k
        else:
            k+=1