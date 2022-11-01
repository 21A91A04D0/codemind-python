n=int(input())
x=list(map(int,input().split()))
cnt=0
for i in range(1,len(x)-1):
    if x[i]%2==1 and x[i-1]%2==1 and x[i+1]%2==1:
        cnt+=1
print(cnt)