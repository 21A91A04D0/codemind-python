def fun(ch):
    st='aeiouAEIOU'
    cnt=0
    for i in ch:
        if i in st:
            cnt+=1
    return cnt
s=input()
k=s.split()
d=list(k)
a=[]
for i in d:
        a.append(fun(i))
print(max(a))
        