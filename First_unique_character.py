s=input()
d=list(s)
a=[]
for i in d:
    if d.count(i)==1 and i.islower() or d.count(i)==1 and i.isupper():
        a.append(i)
        break
if len(a)==0:
    print("-1")
else:
    print(*a)

    