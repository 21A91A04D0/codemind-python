s=input()
a=[]
for i in s:
    if i.isdigit():
        a.append(i)
c=0
for i in a:
    c+=int(i)
print(c)