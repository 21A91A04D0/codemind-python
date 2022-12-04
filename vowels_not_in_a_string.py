s=input()
a=['a','e','i','o','u']
cnt=0
for i in s:
    if i in a:
        cnt+=1
        a.remove(i)
if len(a)==0:
    print("0")
else:
    print(*a)
