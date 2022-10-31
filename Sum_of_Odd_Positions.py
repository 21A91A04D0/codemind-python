n=int(input())
lst=list(map(int,input().split()))
sum=0
for i in range(len(lst))[:n]:
    if i%2==1:
        sum=sum+lst[i]
print(sum)