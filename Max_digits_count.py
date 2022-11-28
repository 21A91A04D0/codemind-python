n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    c=0
    while i:
        i//=10
        c+=1
    a.append(c)
print(a.count(max(a)))