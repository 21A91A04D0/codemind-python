def palind(i):
    p=0
    while i:
        d=i%10
        p=p*10+d
        i=i//10
    return p
        
m=int(input())
n=int(input())
for i in range(m,n+1):
    pol=palind(i)
    if pol==i:
        print(pol,end=" ")