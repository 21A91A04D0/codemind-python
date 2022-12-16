r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]
for i in range(r):
    value=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=value[j]
k=[0 for i in range(r)]
for i in range(r):
    for j in range(c):
        k[i]+=d[i][j]
print(*k)
        