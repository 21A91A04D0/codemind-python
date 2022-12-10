n=int(input())
x=list(map(int,input().split()))
ec=0
oc=0
for i in x:
    if i%2:
        oc+=1
    else:
        ec+=1
print(ec,oc)