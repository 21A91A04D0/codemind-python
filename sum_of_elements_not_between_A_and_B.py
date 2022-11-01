n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
sum=0
for i in range(len(x)):
    if x[i]<a or x[i]>b:
        sum=sum+x[i]
print(sum)