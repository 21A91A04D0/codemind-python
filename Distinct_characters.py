s=input()
a=s.replace(' ','')
b=[]
for i in a:
    if i not in b and i.islower():
        b.append(i)
b.sort()
f=''.join(b)
print(f)
