n=int(input())
x=list(map(int,input().split()))
k=int(input())
k=k%n
print(*x[-k:]+x[:-k])