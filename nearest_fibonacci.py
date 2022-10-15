n=int(input())
p=n
a=0
b=1
sum=0
for i  in range(n):
    sum=sum+a
    a=b
    b=sum
    if sum>=n:
        break
    k=sum
z=sum
c=p-k
d=z-p
if c<d:
    print(k)
elif d<c:
    print(z)
elif c==d:
    print(k,z)