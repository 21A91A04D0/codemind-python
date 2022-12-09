def fun(s):
    e=[]
    ind=[]
    v='aeiou'
    for i in range(len(s)):
        if s[i] in v:
            ind.append(i)
        else:
            e.append(s[i])
    e.sort()
    for i in ind:
        e.insert(i,s[i])
    f=''.join(e)
    return f
s=input()
k=s.split()
a=[]
for i in k:
    a.append(fun(i))
print(*a)
    
    