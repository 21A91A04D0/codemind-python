def reverse(n):
    sq=n*n#169
    r=n#13
    s=0
    while n:
        d=n%10
        s=s*10+d
        n=n//10
    rev=s#31
    squ=rev*rev#961
    a=0
    while squ:
        d=squ%10
        a=a*10+d
        squ=squ//10
    revn=a
    if revn==sq:
        return True
    else:
        return False
        
n=int(input())
print(reverse(n))