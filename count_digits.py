n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    a.append(abs(i))
for j in a:
    c=0
    if j==0:
        c+=1
    while j>=1:
        c+=1
        j//=10
    b.append(c)

print(*b)