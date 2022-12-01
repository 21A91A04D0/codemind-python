n=input()
a='aeiouAEIOU'
b=' '
d=' '
c=0
for i in n:
    if i in a:
        c+=1
        b+=i
for i in b:
    if i not in d:
        d+=i
        print(i,end=' ')
    
if c==0:
    print("-1")
