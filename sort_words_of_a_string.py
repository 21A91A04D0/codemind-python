def fun(s):
    ind=[]
    e=[]
    for i in range(len(s)):
        if s[i].isalpha():
            e.append(s[i])
        else:
            ind.append(i)
    e.sort()
    for i in ind:
        e.insert(i,s[i])
    f=''.join(e)
    return f
            
        
k=input()
d1=k.split()
a=[]
for i in d1:
    a.append(fun(i))
print(*a)
    