n=int(input())
t=0
i=1
while(i<n):
    x=n%i
    if x==0:
        t=t+i
    i+=1
if t==n:
    print("True")
else:
    print("False")
    

        
        