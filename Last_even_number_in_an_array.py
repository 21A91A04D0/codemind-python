n=int(input())
lst=list(map(int,input().split()))
for i in range(len(lst)):
    if lst[i]%2==0:
        a=lst[i]
print(a)