#разрыв
for x in [k * 0.25 for k in range(-10000, 10000)]:
    P = 3 <= x <= 15
    Q = 14 <= x <= 25
    A=1
    f=(P == Q)<= (not A)
    if f != 0:
        print(x) # [3,14) and (15,25] 11 - max 