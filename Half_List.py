n=int(input())
x=list(map(int,input().split()))
a=[]
b=[]
for i in range(0,(n//2)):
    a.append(x[i])
for j in range(n//2,len(x)):
    b.append(x[j])
b.reverse()
for i in a:
    b.append(i)
print(*b)
    
    