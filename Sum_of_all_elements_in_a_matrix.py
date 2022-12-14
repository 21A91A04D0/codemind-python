r,c=map(int,input().split())
row=[0 for i in range(c)]
a=[row.copy() for i in range(r)]
sum=0
for i in range(r):
    vals=list(map(int,input().split()))
    for j in range(c):
        a[i][j]=vals[j]
        sum+=vals[j]
print(sum) 
