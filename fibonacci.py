n=int(input())
a=0
b=1
sum=0
for i in range(n):
    sum=sum+a#0
    a=b#1
    b=sum#0
    print(sum,end=" ")
    