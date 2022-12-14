def fun(d,r,c):
    ev=0
    odd=0
    for i in range(r):
        for j in range(c):
            if d[i][j]%2==0:
                ev+=d[i][j]
            else:
                odd+=d[i][j]
    return ev,odd
r,c=map(int,input().split())
row=[0 for i in range(c)]
col=[row.copy() for i in range(r)]
for i in range(r):
    vals=list(map(int,input().split()))
    for j in range(c):
        col[i][j]=vals[j]
res=fun(col,r,c)
print(*res)