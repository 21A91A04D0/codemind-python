import math
def sq(n):
    p=n
    squ=int(math.sqrt(n))
    r=squ*squ
    if r==p:
        return True
    else:
        return False
    
    
n=int(input())
print(sq(n))