def fun(ch):
    a=min(ch)
    b=max(ch)
    c=ord(a)
    d=ord(b)
    return(abs(c-d))
    
s=input()
k=s.split()
a=[]
for i in k:
    a.append(fun(i))
print(*a)