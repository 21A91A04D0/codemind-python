def fun(d,r,c):
    ev_cnt=0
    odd_cnt=0
    for i in range(r):
        for j in range(c):
            if i%2==0:
                ev_cnt+=d[i][j]
            else:
                odd_cnt+=d[i][j]
    return ev_cnt,odd_cnt
r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]
for i in range(r):
    vals=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=vals[j]
res=fun(d,r,c)
print(*res)