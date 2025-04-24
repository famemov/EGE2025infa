def f(x,y,h):
    if (h==3) and (x+y>=86):
        return 1
    if (h==3) and (x+y<86):
        return 0
    if (x+y>=86):
        return 0
    
    if h%2==0:
        return f(x+1,y,h+1) or f(x*2,y,h+1) or f(x,y+1,h+1) or f(x,y*2,h+1)
    else:
        return f(x+1,y,h+1) and f(x*2,y,h+1) and f(x,y+1,h+1) and f(x,y*2,h+1)
    
for s in range(1,72):
    if f(14,s,0):
        print(s)