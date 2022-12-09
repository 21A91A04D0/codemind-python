s=input()
a=s.replace(' ','')
b=list(a)
a=[]
for i in b:
    if i.islower() and b.count(i)==1:
        a.append(i)
print(len(a))
    