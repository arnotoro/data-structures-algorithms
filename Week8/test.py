import random

def algorithm(L):
    k = 0
    for i in range(1,L):
        x = random.randint(0,1)
        y = random.randint(0,1)
        if (x^2 + y^2 < 1):
            k = k + 1
    return (4 * k) /L


print(algorithm(10000000))

