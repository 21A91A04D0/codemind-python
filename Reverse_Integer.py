def reverse(num):
    s=0
    while num:
        d=num%10
        s=s*10+d
        num=num//10
    return s
        
n=int(input())
s=0
if n<0:
    s=2
n=abs(n)
n=reverse(n)
if s==2:
    print(-n)
else:
    print(n)
