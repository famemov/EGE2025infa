def f(x, A):
    return ((x & 45 >0)or(x&89>0))<=(x&A>0)

print(min(A for A in range(0,200) if all(f(x,A)==1 for x in range(0,2000))))