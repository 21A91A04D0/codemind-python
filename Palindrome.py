def palind(n):
    z=n
    rev=0
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    if rev==z:
        return True
    else:
        return False
n=int(input())
print(palind(n))