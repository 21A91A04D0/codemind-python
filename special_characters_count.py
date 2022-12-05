s=input()

cnt=0
for i in s:
    if ord(i)>=97 and ord(i)<=122 or ord(i)>=65 and ord(i)<=90 or ord(i)==32:
        cnt+=1
a=len(s)

print(a-cnt)