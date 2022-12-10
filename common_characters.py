s1=input()
s2=input()
a1=s1.lower()
a2=s2.lower()
s=[]
for i in a1:
    if i in a2 and i not in s and i!=' ':
        s.append(i)
s.sort()
b=''.join(s)
if len(s)==0:
    print("-1")
else:
    print(b)
        