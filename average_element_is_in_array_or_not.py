n=int(input())
x=list(map(int,input().split()))
a=sum(x)
b=(a//n)
for i in range(len(x)):
    if b==x[i]:
        print("True")
        break
else:
    print("False")