n=int(input())
x=list(map(int,input().split()))
sum=0
for i in range(len(x)):
    if x[i]%2==0:
        sum=sum+x[i]
a=sum
s=0
for i in range(len(x)):
    if x[i]%2==1:
        s+=x[i]
b=s
print(abs(a-b))