n=int(input())
x=list(map(int,input().split()))
a=sum(x)
b=a//n
ct=0
for i in range(0,len(x)):
    if x[i]>=b:
        ct+=1
print(ct)