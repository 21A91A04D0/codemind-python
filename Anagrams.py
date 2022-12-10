s1=input()
s2=input()
d=[0]*26
for i in s1:
    if ord(i)>=97 and ord(i)<=122:
        asc=ord(i)-97
    else:
        asc=ord(i)-65
    d[asc]+=1
for i in s2:
    if ord(i)>=97 and ord(i)<=122:
        asc=ord(i)-97
    else:
        asc=ord(i)-65
    d[asc]-=1
for i in d:
    if i!=0:
        print(False)
        break
else:
    print(True)
