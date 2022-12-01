n=input()
a=n.split()
b=list(a)
for i in range(0,len(b)):
    if i%2==0:
        print(b[i][::-1],end=' ')
    else:
        print(b[i],end=' ')
    

    