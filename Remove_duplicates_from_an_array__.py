n=int(input())
x=list(map(int,input().split()))
a=[]
for i in x:
   if i not in a:
       a.append(i)
print(*a)