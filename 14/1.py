a='012345678'
for x in a:
    for y in a:
        s1=int('88'+x+'4'+y,9)
        s2=int('7'+x+'44'+y,11)
        s=s1+s2
        if s %61==0:
            print(s//61)
print(bin(9))