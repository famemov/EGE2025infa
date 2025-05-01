def f(x,h):
    if (h==2) and (x>=24): return 1
    if (h==2) and (x<24): return 0
    if (x>=24): return 0
    if (h%2==0): return f(x+1,h+1) or f(x+2,h+1) or f(x*2,h+1)
    else: return f(x+1,h+1) or f(x+2,h+1) or f(x*2,h+1)

for s in range(1,24):
    if f(s,0):
        print(s)