x=input()
c=0
for i in x:
    if i==" ":
        print(c,end=" ")
        c=0
        continue
    c+=1
print(c)