N=int(input())
temp=N
for i in range(1,N):
    m=i**2
    if temp==m:
        print("True")
        break
else:
    print("False")