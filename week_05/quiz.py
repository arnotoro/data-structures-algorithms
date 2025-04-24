def recursion(x):
    if x == 0:
        return 1
    else:
        return recursion(x-1) + recursion(x-1)


if __name__ == '__main__':
    value = int(input("Give value: "))
    print(recursion(value))
