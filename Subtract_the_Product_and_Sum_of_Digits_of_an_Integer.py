def res(n):
    p=1
    s=0
    while n:
        d=n%10
        p=p*d
        s=s+d
        n=n//10
    return p-s
n=int(input())
spd=res(n)
print(spd)