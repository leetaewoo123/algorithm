str1 = input()
str2 = ''
for i in range (len(str1)):
    if str1[i].isupper():
        str2 += str1[i].lower()
    else:
        str2 += str1[i].upper()
        
print(str2)
