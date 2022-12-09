s=input()
a=s.replace(' ','')
d=list(a)
a=[]
for i in d:
    if i not in a and i.islower():
        a.append(i)
print(len(a))