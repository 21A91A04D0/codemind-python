def fun(c,k):
    j=1
    cnt=0
    while j<len(k):
        if c in k[j]:
            cnt+=1
        j+=1
    return cnt
            
            
            
s1=input()
a1=s1.lower()
k=a1.split()
d=k[0]
a=[]
for i in d:
    res=fun(i,k)
    if res==len(k)-1:
        a.append(i)
if len(a)==0:
    print("-1")
else:
    f=''.join(a)
    print(f)
        
    
