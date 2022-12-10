def fun(ind,s,d):
    s1=''
    cnt=0
    for i in range(len(s)-1,-1,-1):
        s1+=s[i]
    if s1==d[ind]:
        cnt+=1
    return cnt   
        
        
k=input()
s=k.lower()
d=s.split()
ct=0
for i in range(len(d)):
    if fun(i,d[i],d):
        ct+=1
print(ct)
    