import math
n=int(input())
x=list(map(int,input().split()))
a=[]
sum=0
for i in x:
    sq=int(math.sqrt(i))
    if i==sq*sq:
        sum+=i
print(sum)