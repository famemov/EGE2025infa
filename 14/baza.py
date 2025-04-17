x=12312
print(bin(x)[2:])

s=''
while x>0:
    s+=str(x%2)
    x=x//2


print(s[::-1])

print(int(s[::-1],2))