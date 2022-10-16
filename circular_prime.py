import math
def isprime(n):
    if n==1:
        return False
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
    
def reverse(n):
    s=0
    while n:
        d=n%10
        s=s*10+d
        n=n//10
    return s
n=int(input())
if isprime(n):
    n=reverse(n)
    if isprime(n):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")