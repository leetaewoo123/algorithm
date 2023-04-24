def solution(park, routes):
    answer = []
    for i in park:
        if "S" in i:
            s  = [park.index(i),i.index("S")]
            break

    for i in routes:
        n = 0
        if i[0] == "E" and s[1] + int(i[2]) < len(park[0]):
            for j in range (int(i[2])):
                if park[s[0]][s[1]+(j+1)] == "X":
                    n+=1
            if n == 0:
                s[1] += int(i[2])
                        
        if i[0] == "W" and s[1] - int(i[2]) >= 0:
            for j in range (int(i[2])):
                if park[s[0]][s[1]-(j+1)] == "X":
                    n+=1
            if n==0:
                s[1] -= int(i[2])
                        
        if i[0] == "S" and s[0] + int(i[2]) < len(park):
            for j in range (int(i[2])):
                if park[s[0]+(j+1)][s[1]] == "X":
                    n+=1 
            if n == 0:
                s[0] += int(i[2])
                        
        if i[0] == "N" and s[0] - int(i[2]) >= 0:
            for j in range (int(i[2])):
                if park[s[0]-(j+1)][s[1]] == "X":
                    n+=1
            if n == 0:
                s[0] -= int(i[2])

    return s



# console.log(solution(["OSO","OOO","OOO","OOO"], ["N 2"])); // [0,1]
# console.log(solution(["OSO","OOO","OOO","OOO"], ["S 5"])); // [0,1]
# console.log(solution(["OSO","OOO","OOO","OOO"], ["E 5"])); // [0,1]

# console.log(solution(["XXX","XSX","XXX"], ["E 1"])); // [1,1]
# console.log(solution(["XXX","XSX","XXX"], ["W 1"])); // [1,1]
# console.log(solution(["XXX","XSX","XXX"], ["S 1"])); // [1,1]
# console.log(solution(["XXX","XSX","XXX"], ["N 1"])); // [1,1]

# console.log(solution(["SOXOO","OOOOO","OOOOO", "OOOOO", "OOOOO"], ["E 3"])); // [0, 0]
# console.log(solution(["SOOOX","OOOOO","OOOOO", "OOOOO", "OOOOO"], ["E 3"])); // [0, 3]
# console.log(solution(["XOOOS","OOOOO","OOOOO", "OOOOO", "OOOOO"], ["W 3"])); // [0, 1]
# console.log(solution(["OOXOS","OOOOO","OOOOO", "OOOOO", "OOOOO"], ["W 3"])); // [0, 4]
# console.log(solution(["SOOOO","OOOOO","XOOOO", "OOOOO", "OOOOO"], ["S 3"])); // [0, 0]
# console.log(solution(["SOOOO","OOOOO","OOOOO", "OOOOO", "XOOOO"], ["S 3"])); // [3, 0]
# console.log(solution(["OOOOO","OOOOO","XOOOO", "OOOOO", "SOOOO"], ["N 3"])); // [4, 0]
# console.log(solution(["XOOOO","OOOOO","OOOOO", "OOOOO", "SOOOO"], ["N 3"])); // [1, 0]