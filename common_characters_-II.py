s1=input()
s2=input()
a1=s1.lower()
a2=s2.lower()
s=[]
a=[]
for i in a1:
    if i in a2 and i!=' ' and i not in s:
        s.append(i)
print(len(s))