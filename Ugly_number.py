def ugly_number(n):
    while n%2==0:
        n=n//2
    if n==1:
        return True
    while n%3==0:
        n=n//3
    if n==1:
        return True
    while n%5==0:
        n=n//5
    if n==1:
        return True
        
        
n=int(input())
if ugly_number(n):
    print("Ugly Number")
else:
    print("Not Ugly Number")