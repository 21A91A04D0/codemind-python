N=int(input())
rev=0
while N:
    dig=N%10
    rev=rev*10+dig
    N=N//10
print(rev)