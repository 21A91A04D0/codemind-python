import math
a,b,c=map(float,input().split())
s=(a+b+c)/2
p=float(math.sqrt(s*(s-a)*(s-b)*(s-c)))
print(format(p,".2f"))