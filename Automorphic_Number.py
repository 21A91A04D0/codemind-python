def autom(n):
    s=n*n
    on=0
    a=1
    while s:
        d=s%10#6
        s=s//10#576
        on=on+a*d
        a=a*10
        if on==n:
            return True
        continue
        return False
            
n=int(input())
num=autom(n)
if autom(n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    
