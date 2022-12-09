s=input()
a=s.replace(' ','')
d=list(a)
d.sort()
s1=''
for i in d:
    if i.islower() and d.count(i)==1:
        s1+=i
print(s1)