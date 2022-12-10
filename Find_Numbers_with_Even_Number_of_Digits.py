def count(n):
    c=0
    while n:
        d=n%10
        n=n//10
        c+=1
    return c
n=int(input())
x=list(map(int,input().split()))
l=[]
for i in x:
    l.append(count(i))
ct=0
for i in l:
    if i%2==0:
        ct+=1
print(ct)