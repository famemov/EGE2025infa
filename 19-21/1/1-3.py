def f(x,h):
    if (h==2 or h==4) and (x>=63):
        return 1
    if (h==4) and (x<63):
        return 0
    if (x>=63):
        return 0
    if (h%2==0):
        return f(x+1,h+1) and f(x+4,h+1) and f(x*5,h+1)
    else: 
        return f(x+1,h+1) or f(x+4,h+1) or f(x*5,h+1)

for s in range(1,63):
    if f(s,0):
        print(s)