n=int(input())
x=list(map(int,input().split()))
a=[]
for i in x:
    a.append(i)
a.sort()
print(*a)
    