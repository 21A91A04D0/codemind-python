def array(p,lst):
    
    a=[]
    for i in lst:
        if p==i:
            continue
        else:
            a.append(i)
    val=1        
    for i in a:
        val=val*i
    return val
    
n=int(input())
x=list(map(int,input().split()))
p=0
for i in x:
    p=i
    print(array(p,x),end=' ')
    
    