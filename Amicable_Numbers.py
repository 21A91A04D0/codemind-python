def amicable(m,n):
    a=n
    b=m
    sum=0
    for i in range(1,m):
        if m%i==0:
            sum=sum+i
    p=sum
    q=0
    for i in range(1,n):
        if n%i==0:
            q=q+i
    z=q
    if p==a and z==b:
        return "Amicable"
    else:
        return "Not Amicable"

m=int(input())
n=int(input())
print(amicable(m,n))