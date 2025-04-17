for x in [k * 0.25 for k in range(-10000,10000)]:
    P=10<=x<=40
    Q=5<=x<=15
    R=35<=x<=50
    A=0
    f=(A or P)or(Q <= R)
    if f!=1:
        print(x)#[5,10)