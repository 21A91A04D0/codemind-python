n=int(input())
x=list(map(int,input().split()))
evens=[]
for i in range (len(x)):
    if i%2==0:
        evens.append(x[i])
for j in evens:
    if j%2==1:
        print("False")
        break
else:
    print("True")