def count(n):
    cnt=0
    while n:
        d=n%10
        cnt+=1
        n=n//10
    return cnt
def reverse(n):
    revs=0
    while n:
        d=n%10
        revs=revs*10+d
        n=n//10
    return revs
n,x=map(int,input().split())
f=n
ct=0
rev=0
a=1
z=0
while n:
    d=n%10
    ct+=1
    rev=d*a+rev
    n=n//10
    a=a*10
    if count(rev)==x:
        z=rev
k=reverse(f)
ct1=0
rev1=0
z1=0
while k:
    d=k%10
    ct1+=1
    rev1=rev1*10+d
    k=k//10
    if count(rev1)==x:
        z1=rev1
print(abs(z-z1))
        
    
    
    