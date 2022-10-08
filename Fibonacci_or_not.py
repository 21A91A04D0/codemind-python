def fib(n):
    a=0
    b=1
    sum=0
    for i in range(n):
        sum=sum+a#0
        a=b#1
        b=sum#0
        if sum==n:
           return True
n=int(input())
if fib(n):
    print("True")
else:
    print("False")
