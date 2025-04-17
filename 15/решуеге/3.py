for x in [k * 0.25 for k in range(-10000,10000)]:
    P= 5 <= x <= 30
    Q= 14 <= x <= 23
    A=1
    f=(P==Q)<= (not A)
    if f!=0:
        print(x)#[5,14) (23,30] 9 7 ответ:9