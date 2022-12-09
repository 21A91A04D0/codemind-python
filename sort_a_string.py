s=input()
ind=[]
d=[]
for i in range(len(s)):
    if s[i].isalpha():
        d.append(s[i])
    else:
        ind.append(i)
k=sorted(d)
for i in ind:
    k.insert(i,s[i])
print(''.join(k))