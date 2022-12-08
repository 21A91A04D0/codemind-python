def fun(ch):
    vowels='aeiouAEIOU'
    cnt=0
    for i in ch:
        if i in vowels:
            cnt+=1
    return cnt
s=input()
k=s.split()
a=[]
for i in k:
    a.append(fun(i))
t=max(a)
ct=0
for i in a:
    if i==t:
        ct+=1
print(ct)