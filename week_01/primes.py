def primes(N):
    result = 0

    for i in range(2, N+1):
        prime = True

        # Check prime
        for j in range(2, i):
            if (i % j == 0):
                prime = False
                break
        
        if (prime):
            result += 1

    return result


if __name__ == "__main__":
    print(primes(7))    # 4
    print(primes(15))   # 6
    print(primes(50))   # 15
    print(primes(100))  # 25
    