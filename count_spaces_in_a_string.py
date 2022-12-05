s=input()
cnt=0
for i in s:
    if ord(i)==32:
        cnt+=1
print(cnt)