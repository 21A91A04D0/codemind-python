n=int(input())
x=list(map(int,input().split()))
a=n-1
sum=0
for i in x:
    sum+=i*(2**a)
    a-=1
print(sum)