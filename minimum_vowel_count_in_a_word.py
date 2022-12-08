def fun(ch):
    str='aeiouAEIOU'
    cnt=0
    for i in ch:
        if i in str:
            cnt+=1
    return cnt
s=input()
k=s.split()
a=[]
for i in k:
    a.append(fun(i))
print(min(a))