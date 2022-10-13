def palind(n):
    rev=0
    temp=n
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    if rev==temp:
        return True
    else:
        return False
n=int(input())
print(palind(n))