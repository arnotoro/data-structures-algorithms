def cut_rod1(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(n):
        q = max(q, p[i] + cut_rod1(p, n-1))
    return q

def cut_rod2(p, n):
    r = []
    r.insert(0,0)
    for j in range(n):
        q = float('-inf')
        for i in range(j):
            q = max(q, p[i] + r[j-i])
            r[j] = q
    return r[n]

p = [1, 5, 8, 9]


print(cut_rod1(p, 4))
print(cut_rod2(p, 4))

