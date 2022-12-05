for i in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    t=n-1
    s=0
    a=[]
    for i in range(n):
        if i%2==0:
            a.append(x[t])
            t-=1
        else:
            a.append(x[s])
            s+=1
    print(*a)
    

        
        
        
            
    
    