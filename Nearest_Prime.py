import math
def isprime(n):
    sq=int(math.sqrt(n))
    for j in range(2,sq+1):
        if n%j==0:
            return False
    return True
for i in range(int(input())):
    n=int(input())
    for k in range(n,0,-1):
        if isprime(k):
            break
    for l in range(n,n*n):
        if isprime(l):
            break
    a=n-k
    b=l-n
    if a<b:
        print(k)
    elif b<a:
        print(l)
    elif a==b:
        print(k)
    