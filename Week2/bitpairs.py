def pairs(s):
    ones = []
    for i in range(len(s)):
        if s[i] == "1":
            ones.append(i)

    print(ones)
    result = 0

    for i in range(1, len(ones)):
        print(ones[i], ones[i - 1], end=" ")
        result += abs(ones[i] - ones[i - 1])
        print(result)

    return result

if __name__ == "__main__":
    print(pairs("100101")) # 10
    print(pairs("101")) # 2
    print(pairs("100100111001")) # 71
