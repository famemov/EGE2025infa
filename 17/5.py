a=[int(x) for x in open('17.txt')]

even = [s for s in a if s%2==0]
m=sum(even)/len(even)
k=0
r=[]

for i in range(0, len(a)-1):
    if ((a[i] %3)==0  and a[i+1]<m) or ( (a[i+1]%3)==0 and a[i]<m):
        k+=1
        r.append(a[i]+a[i+1])

print(k, max(r))