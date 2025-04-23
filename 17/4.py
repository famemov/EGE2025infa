a=[int(x) for x in open('17/17_18617.txt')]
mx=max(a)
mn=min(a)
k=0
r=[]


for i in range(len(a)-1):
    if a[i]%3==mx%3 or a[i+1]%3==mx%3:
        if a[i]%7==mn%7 or a[i+1]%7==mn%7:
            k+=1
            r.append(a[i]+a[i+1])
print(k, max(r))
