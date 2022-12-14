n=int(input())
row=[0 for i in range(n)]
a=[row.copy() for i in range(n)]
b=[row.copy() for i in range(n)]
c=[row.copy() for i in range(n)]
sum=0
for i in range(n):
    vals=list(map(int,input().split()))
    for j in range(n):
        a[i][j]=vals[j]
        
for i in range(n):
    value=list(map(int,input().split()))
    for j in range(n):
        b[i][j]=value[j]
for i in range(n):
    for j in range(n):
        c[i][j]=abs(b[i][j]-a[i][j])
for i in c:
    print(*i)