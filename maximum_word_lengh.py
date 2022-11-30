x=input()
a=x.split()
s=[]
c=[]
for i in a:
    s.append(i)
for j in s:
    c.append(len(j))
print(max(c))
    