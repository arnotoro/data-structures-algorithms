def towerOfHanoi(n, start, finish, extra):
    if(n == 1):
        print("Move disk 1 from rod",start,"to rod",finish)
        return
    towerOfHanoi(n-1, start, extra, finish)
    print("Move disk",n,"from rod",start,"to rod",finish)
    towerOfHanoi(n-1, extra, finish, start)



disks = int(input("How many disks: "))
towerOfHanoi(disks,'A','C','B')
