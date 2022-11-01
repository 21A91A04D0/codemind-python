n=int(input())
maxm=[]
x=list(map(int,input().split()))
a,b=map(int,input().split())

for i in x:
    if i<a or i>b:
        maxm.append(i)
if i>a and i<b:
    print("-1")
print(max(maxm))