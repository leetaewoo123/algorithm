def solution(cacheSize, cities):
    answer = 0
    time,c,city = 0, [],[]
    for i in cities:
        city.append(i.upper())
    if cacheSize != 0:
        for i in range(len(city)):
            if len(c) != cacheSize:
                if city[i] not in c:
                    c.append(city[i])
                    time += 5
                else:
                    c.remove(city[i])
                    c.append(city[i])
                    time += 1
            else:
                if city[i] not in c:
                    del c[0]
                    c.append(city[i])
                    time += 5
                else:
                    c.remove(city[i])
                    c.append(city[i])
                    time += 1
    else :
        time = len(cities)*5
    return time