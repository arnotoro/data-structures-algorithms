def sums(A: list):
    result = {0}

    for number in A:
        new_result = set()
        #iterate over each value in given list and add them together
        #if the value + sum is unique, add it to the set. set holds only unique values
        for value in result:
            new_result.add(value + number)
        result.update(new_result)

    #print(result)
    return len(result) - 1 #-1 to remove 0 from the count



if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2])) # 121