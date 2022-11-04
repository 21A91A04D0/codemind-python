n=int(input())
x=list(map(int,input().split()))
odds_i=[]
for i in range (len(x)):
    if i%2==1:
        odds_i.append(x[i])
for j in odds_i:
    if j%2==0:
        print("False")
        break
else:
    print("True")