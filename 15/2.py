for x in [k*0.25 for k in range(-10000,10000)]:
    P= 43 <= x <= 49
    Q= 44 <= x <= 53
    A=1
    f=(A<=P) or Q
    if f != 0:
        print(x) #43.0 53.0 otvet:10