N=int(input())
res=0
sq=N*N
while sq:
    d=sq%10
    res=res+d
    sq=sq//10
if res==N:
    print("Neon Number")
else:
    print("Not Neon Number")

    