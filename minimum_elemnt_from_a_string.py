s=input()
sm=[]
cp=[]
z=[]
for i in s:
    if i.islower():
        sm.append(i)
    else:
        cp.append(i)
for i in cp:
    if chr(ord(i)+32) in sm:
        z.append(i.lower())
if len(z)==0:
    print(min(s))
elif len(z)!=0:
    print(min(sm))