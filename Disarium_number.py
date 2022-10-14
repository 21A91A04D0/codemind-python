def dis(n):
    s=0
    z=n
    while n:
        d=n%10
        s=s*10+d
        n=n//10
    q=s
    rev=0
    i=1
    while s:
        d=s%10
        rev=rev+(d**i)
        i+=1
        s=s//10
    p=rev
    if p==z:
        return True
    else:
        return False
        
  
    
            
n=int(input())
print(dis(n))