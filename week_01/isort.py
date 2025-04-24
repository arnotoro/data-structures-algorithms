def isort(A):
    if (len(A) > 10000):
        print("Input size too large")
        return
    
    for i in range(len(A)):
        j = i-1
        while (j >= 0) and (A[j] > A[j+1]):
            A[j], A[j+1] = A[j+1], A[j]
            j = j-1


if __name__ == "__main__":
    A = [4, 3, 6, 2, 9, 7, 1, 8, 5]
    isort(A)
    print(A) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
