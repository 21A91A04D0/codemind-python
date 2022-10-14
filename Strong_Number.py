def strong(n):
    s=0
    z=n
    while n:
        d=n%10
        f=1
        for i in range(1,d+1):
            f=i*f
        s=s+f
        n=n//10
    if z==s:
        return "The number %(z)d is a strong number"%{"z":z}
    else:
        return "The number %(z)d is not a strong number"%{"z":z}
        
            
n=int(input())
print(strong(n))
    