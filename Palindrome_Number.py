for i in range(int(input())):
    n=int(input())
    n=abs(n)
    p=n
    rev=0
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    if p==rev:
        print("True")
    else:
        print("False")