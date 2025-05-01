def f(x,h):
    if (h==2 or h==4) and (x>=50): return 1
    if h==4 and x<50: return 0
    if x>=50: return 0
    if h%2==0: return f(x+1,h+1) and f(x+3,h+1) and f(x*2,h+1)
    else: return f(x+1,h+1) or f(x+3,h+1) or f(x*2,h+1)

for s in range(1,50):
    if f(s,0):
        print(s)