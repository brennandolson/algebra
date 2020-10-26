from collections import defaultdict as dd

class number:
    ints  = [2, 3]
    roots = [2, 3]
    def __init__(self, d = None):
        if not d:
            self.c = dd(int) # coefficients
        else:
            self.c = d
    

    def set(self, k, v):
        self.c[k] = v
    

    def add(self, k, v):
        self.c[k] += v


    def get(self, k):
        return self.c[k]


    def __add__(self, other):
        new_c = dd(int)
        pos_coeffs = set(self.c.keys()).union(set(other.c.keys()))
        for coeff in pos_coeffs:
            new_c[coeff] = self.c[coeff] + other.c[coeff]
        return number(new_c)

    
    def __str__(self):
        return self.c.__repr__()

    
    def coeff_row(self):
        ret = []
        for p1 in range(self.roots[0]):
            for p2 in range(self.roots[1]):
                ret.append(self.c[(p1, p2)])
        return " ".join(map(str, ret))

    def __mul__(self, other):
        res = number()
        ints = self.ints
        roots = self.roots
        for k1, v1 in self.c.items():
            for k2, v2 in other.c.items():
                new_k = [0] * len(ints)
                new_v = v1 * v2
                for i in range(len(ints)):
                    new_k[i] = k1[i] + k2[i]
                    if new_k[i] >= roots[i]:
                        new_k[i] -= roots[i]
                        new_v *= ints[i]
                res.add(tuple(new_k), new_v)

        return res

x = number()
x.set((1, 0), 1)
x.set((0, 1), 1)

y = number()
y.set((0, 0), 1)
for i in range(7):
    print (y.coeff_row())
    y = y * x

# print (x*x*x)
# print (x.coeff_row())
# x = number()
# y = number()
# x.set((1, 1), 2)
# y.set((1, 1), 3)
# y.set((0, 2), 0)
# print (x)
# print (y)
# 
# print (x + y)
