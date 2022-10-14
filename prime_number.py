def isprime(n):
    pc=0
    for i in range(1,n+1):
        if n%i==0:
            pc+=1
    if pc==2:
        return "prime"
    else:
        return "not a prime"
n=int(input())
print(isprime(n))