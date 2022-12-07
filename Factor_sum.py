def fun(n):
    s=0
    for j in range(1,n+1):
        if n%j==0:
            s+=j
    return s
x=list(map(int,input().split(',')))
a=[]
for i in x:
    if fun(i) in x:
        a.append(i)
a.sort()
if len(a)==0:
    print("-1")
else:
    print(*a)
        
    
    
