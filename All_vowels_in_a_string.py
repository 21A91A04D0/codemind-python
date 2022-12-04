s=input()
a=['a','e','i','o','u']
b=['A','E','I','O','U']
k=[]
l=[]
z=set()
x=set()
for i in s:
    if i in a:
        k.append(i)
    if i in b:
        l.append(i)
k.sort()
l.sort()
for i in k:
    z.add(i)
for i in l:
    x.add(i)
if len(z)==len(a) or len(z)==len(b):
    print("True")
elif len(x)==len(a) or len(x)==len(b):
    print("True")
else:
    print("False")

    
        
        
