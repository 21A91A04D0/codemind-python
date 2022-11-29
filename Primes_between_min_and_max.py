import math
def prime(num):
    if num==1:
        return False
    sq=int(math.sqrt(num))
    for i in range(2,sq+1):
        if num%i==0:
            return False
    return True
n=int(input())
x=list(map(int,input().split()))
lst=[]
a=min(x)
b=max(x)
for i in range(0,len(x)):
    if a==x[i]:
        z=i
        break
for i in range(0,len(x)):
    if b==x[i]:
        k=i
        break
if z > k:
    z, k = k, z

for i in range(0,len(x)):
    if i>=z and i<=k:
        lst.append(x[i])
c=0
for i in lst:
    if prime(i):
        c+=1
print(c)
