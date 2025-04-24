def f(x,y,h):
    if (h==2) and (x+y>=59):
        return 1
    if (h==2) and (x+y<59):
        return 0
    if (x+y>=59):
        return 0
    
    if h%2==0:
        return f(x+1,y,h+1) or f(x*2,y,h+1) or f(x,y+1,h+1) or f(x,y*2,h+1)
    else:
        return f(x+1,y,h+1) or f(x*2,y,h+1) or f(x,y+1,h+1) or f(x,y*2,h+1)

for s in range(1,54):
    if f(5,s,0):
        print(s)