r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]
for i in range(r):
    vals=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=vals[j]
res=0
j=0
for i in range(c):
        res+=d[i][i]
        res+=d[i][c-j-1]
        if d[i][i]==d[i][r-j-1]:
            res-=d[i][i]
        j+=1
print(res)
    