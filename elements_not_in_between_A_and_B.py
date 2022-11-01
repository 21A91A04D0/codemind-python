n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
for i in x:
    if i<a or i>b:
        print(i,end=' ')
if i>a and i<b:
    print("-1")