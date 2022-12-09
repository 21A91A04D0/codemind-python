s=input()
k=s.replace(' ','')
a=min(k)
b=max(k)
sc=0
lc=0
for i in k:
    if i==a:
        sc+=1
    elif i==b:
        lc+=1
print(min(k),sc,max(k),lc)
    