s=input()
cnt=0
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        cnt+=1
print(cnt)