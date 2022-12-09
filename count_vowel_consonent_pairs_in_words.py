def fun(ch):
    n=len(ch)
    i=0
    j=n-1
    cnt=0
    v='aeiouAEIOU'
    while i<j:
        if ch[i] in v and ch[j] not in v or ch[i] not in v and ch[j] in v:
            cnt+=1
        i+=1
        j-=1
    return cnt
s=input()
k=s.split()
c=0
for i in k:
    c+=fun(i)
print(c)
    