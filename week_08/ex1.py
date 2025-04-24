def cut_rod1(p, n):
    if n == 0:
        return 0
    q = -2
    for i in range(1, n):
        q = max(q, p[i] + cut_rod1(p, n-1))
    return q

def cut_rod2(p, n):
    r = [0] * (n+1)
    r[0] = 0
    for j in range(1, n):
        q = -9999
        for i in range(1, j):
            q = max(q, p[i] + r[j-i])
        r[j] = q

    return r[n]

if __name__ == "__main__":
    print(cut_rod1([1, 5, 8, 9, 10], 4))
    print(cut_rod2([1, 5, 8, 9, 10], 4))