def revpalin(x):
    rev=0
    z=x
    while x:
        d=x%10
        rev=rev*10+d
        x=x//10
    p=rev
    q=p+z
    a=q
    r=0
    while q:
        d=q%10
        r=r*10+d
        q=q//10
    b=r
    if a==b:
        return a
    else:
        return revpalin(a)
x=int(input())
print(revpalin(x))
