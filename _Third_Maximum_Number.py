n=int(input())
x=list(map(int,input().split()))
a=set()
for i in x:
    a.add(i)
if len(a)<=2:
    print(max(a))
elif len(a)>2:
    a.remove(max(a))
    a.remove(max(a))
    print(max(a))