n=int(input())
while n>=9:#32
    s=0
    while n:
        d=n%10
        s=s+(d**2)
        n=n//10
    n=s
if n==7 or n==1:
    print("True")
else:
    print("False")