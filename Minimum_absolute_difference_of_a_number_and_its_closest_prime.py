import math
def isprime(n):
    if n==1:
        return False
    sq=int(math.sqrt(n))
    for j in range(2,sq+1):
        if n%j==0:
            return False
    return True

n=int(input())
for k in range(n,0,-1):
    if isprime(k):
        break
for l in range(n,n*n):
    if isprime(l):
        break
a=l-n
b=n-k
if a==b:
    print(a)
elif a>b:
    print(b)
elif a<b:
    print(a)