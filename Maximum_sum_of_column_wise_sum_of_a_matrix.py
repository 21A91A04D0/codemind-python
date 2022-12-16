r,c=map(int,input().split())
row=[0 for i in range(r)]
d=[row.copy() for i in range(c)]
for i in range(r):
    vals=list(map(int,input().split()))
    for j in range(c):
        d[j][i]=vals[j]
k=[0 for i in range(c)]
for i in range(c):
    for j in range(r):
        k[i]+=d[i][j]
print(max(k))