def largest(N):
    l=0
    while N:
        d=N%10
        if l<d:
            l=d
        N=N//10
    return l



N=int(input())
res=largest(N)
print(res)