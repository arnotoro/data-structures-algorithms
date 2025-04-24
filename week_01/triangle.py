def triangle(a, b, c):

    # if one side is negative, return False
    if (a <= 0 or b <= 0 or c <= 0):
        return False
    
    # check if the sum of two sides is less than the third side, in this case return False
    if (a + b <= c or a + c <= b or b + c <= a):
        return False
    
    return True

    


if __name__ == "__main__":
    print(triangle(3, 5, 4))    # True
    print(triangle(-1, 2, 3))   # False
    print(triangle(5, 9, 14))   # False
    print(triangle(30, 12, 29)) # True
    