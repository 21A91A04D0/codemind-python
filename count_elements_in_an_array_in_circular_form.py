n=int(input())
x=list(map(int,input().split()))
cnt=0
for i in range(1,n-1):
    if x[i-1]%2==0 and x[i+1]%2==1 or x[i-1]%2==1 and x[i+1]%2==0:
        cnt+=1
if x[0]%2==0 and x[n-2]%2==1 or x[0]%2==1 and x[n-2]%2==0:
    cnt+=1
if x[n-1]%2==0 and x[1]%2==1 or x[n-1]%2==1 and x[1]%2==0:
    cnt+=1
print(cnt)