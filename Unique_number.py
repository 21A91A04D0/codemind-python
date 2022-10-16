def fun(d,num):
    while num:
        p=num%10
        num=num//10
        if d==p:
            return True
    return False
        
    
n=int(input())
s=0#
while n:
    d=n%10
    n=n//10
    if fun(d,s):
        print("Not Unique Number")
        break
    s=s*10+d
else:
    print("Unique Number")