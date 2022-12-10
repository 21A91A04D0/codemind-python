s1=input()
s2=input()
a1=s1.lower()
a2=s2.lower()
s=[]
a=[]
for i in a1:
    if i not in a2 and i!=' ':
        s.append(i)
for j in a2:
    if j not in a1 and i!=' ':
        s.append(j)
for i in s:
    if i not in a:
        a.append(i)
a.sort()
f=''.join(a)
print(f)


