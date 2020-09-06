def str2map(s, n):
    M = [0] * n
    first = -1
    last  = -1
    for c in s.replace("(", ""):
        if c == ")":
            M[last - 1] = first
            first = -1
            last  = -1
        else:
            if first == -1:
                first = int(c)
            if last != -1:
                M[last - 1] = int(c)
            last = int(c)
    for i in range(n):
        if M[i] == 0:
            M[i] = i + 1
    return M


def map2str(M, n, supress=True):
    cycles = []
    seen = set()
    for i in range(1, n + 1):
        if i not in seen:
            seen.add(i)
            cycle = [i]
            j = i
            while M[j-1] != i:
                j = M[j-1]
                seen.add(j)
                cycle.append(j)
            cycles.append(cycle)
    
    out = ""
    for cycle in cycles:
        if not supress or len(cycle) > 1:
            out += "(" + ''.join(map(str, cycle)) + ")"
    return out


def inv(M, n):
    Mi = [0] * n
    for i in range(n):
        Mi[M[i] - 1] = i + 1
    return Mi


def _mult(M1, M2, n):
    M3 = [0] * n
    for i in range(n):
        M3[i] = M2[M1[i]-1]
    return M3

def mult(M, n):
    if len(M) == 1:
        return M[0]
    else:
        return _mult(M[0], mult(M[1:], n), n)


def conjugate(M1, M2, n):
    M = [M2, M1, inv(M2, n)]
    return mult(M, n)

# H and Sigma from problem statement
g = ["(16425)", "(16)(25)(34)"]
gen = [str2map(s, 6) for s in g]
h = ["(12)(35)(46)", "(13)(24)(56)", "(14)(25)(36)", "(15)(26)(34)", "(16)(23)(45)"]
sigma = [str2map(s, 6) for s in h]

# Computing all 10 relevent conjugations
for x in gen:
    for y in sigma:
        print (map2str(x, 6), end = "")
        print (map2str(y,6), end = "")
        print (map2str(x, 6), end = "^{-1} &= ")
        print (map2str(conjugate(y, x, 6), 6), end="\\\\")
        print ()

# Checking the order of H
curr = list(gen)
seen = set()
for perm in curr:
    seen.add(tuple(perm))
while curr:
    nxt = []
    for perm in curr:
        for x in gen:
            px = mult([perm, x], 6)
            if tuple(px) not in seen:
                seen.add(tuple(px))
                nxt.append(px)
    curr = nxt

print (len(seen))


