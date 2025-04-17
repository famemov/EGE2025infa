def f(n,m):
    return n % m == 0

def d(x,A):
    return (not f(x, A)) or (f(x, 6) or (not f(x, 4)))


print(max(A for A in range(0,200) if all(d(x,A)==1 for x in range(1,2000))))

