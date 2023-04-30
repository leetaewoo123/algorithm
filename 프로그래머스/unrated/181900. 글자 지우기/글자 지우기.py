def solution(my_string, indices):
    word = list(my_string)
    for i in indices :
        word[i] = "@"
    return "".join(word).replace("@","")