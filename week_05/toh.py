def towerOfHanoi(n, start, finish, extra, counter=0):
    counter += 1
    if(n == 1):
        print("Move disk 1 from rod",start,"to rod",finish)
        return counter
    towerOfHanoi(n-1, start, extra, finish, counter)
    print("Move disk",n,"from rod",start,"to rod",finish)
    towerOfHanoi(n-1, extra, finish, start, counter)



disks = int(input("How many disks: "))
count = towerOfHanoi(disks,'A','C','B')