s1=input()
s2=input()
a1=s1.lower()
a2=s2.lower()
d1=a1.split()
d2=a2.split()
for i in d2:
    if i in d1:
        print(i,end=' ')