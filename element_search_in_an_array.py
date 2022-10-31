n=int(input())
x=list(map(int,input().split()))
p=int(input())
for i in range(len(x))[:n]:
    if x[i]==p:
        print("True")
        break
else:
    print("False")