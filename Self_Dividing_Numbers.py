def self_div(n,m):
    for i in range(n,m+1):
        if self_di(i):
            print(i,end=" ")
def self_di(a):
    t=a
    while t:
        d=t%10
        t=t//10
        if d==0 or a%d!=0:
            return False
    return True
n=int(input())
m=int(input())
div=self_div(n,m)