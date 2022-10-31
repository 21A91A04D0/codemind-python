n=int(input())
x=list(map(int,input().split()))
sum=0
for i in range(len(x)):
    if x[i]%2==0:
        sum=sum+x[i]
print(sum)