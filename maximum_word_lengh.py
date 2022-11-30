n=input()
c=0
s=[]
for i in n:
    if i==" ":
        s.append(c)
        c=0
        continue
    c+=1
s.append(c)
print(max(s))
    

    