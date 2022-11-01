n=int(input())
x=list(map(int,input().split()))
evens=[]
odds=[]
for i in range(len(x)):
    if x[i]%2==0:
        evens.append(x[i])
    else:
        odds.append(x[i])
evens.extend(odds)
print(*evens)