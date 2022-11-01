n=int(input())
x=list(map(int,input().split()))
odds=[]
evens=[]
for i in range(len(x)):
    if x[i]%2==1:
        odds.append(x[i])
    else:
        evens.append(x[i])
odds.extend(evens)
print(*odds)