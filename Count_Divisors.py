i,r,k=map(int,input().split())
ct=0
for num in range(i,r+1):
    if num%k==0:
        ct+=1
print(ct)
    