def pairs(s):
    result = 0
    ones = []

    for i in range(len(s)):
        if s[i] == "1":
            ones.append(i)

    i = 0
    j = 1

    while j < len(ones):
        result += ones[j] - ones[i]
        j += 1
        i += 1

    return result

# Example usage:
print(pairs("100101"))        # Output: 10
print(pairs("101"))           # Output: 2
print(pairs("100100111001"))  # Output: 71
