def jumps(n, a, b):
    resultList = [0] * (n + 1)
    resultList[0] = 1 #only 1 way to reach level 0
    
    for level in range(1, n + 1):
        #check if jump is possible at current level with a or b
        #if the jump is possible add up the number of ways to reach the previous level to the current level in the lsit
        #print(level)
        if level - a >= 0:
            #print(level, a, level - a)
            resultList[level] += resultList[level - a]
        if level - b >= 0:
            #print(level, b, level - b)
            resultList[level] += resultList[level - b]

    #print(resultList)

    #last element is the result
    return resultList[n]
    


if __name__ == "__main__":
    
    print(jumps(4, 1, 2)) # 5
    print(jumps(8, 2, 3)) # 4
    print(jumps(11, 6, 7)) # 0
    print(jumps(30, 3, 5)) # 58
    print(jumps(100, 4, 5)) # 1167937