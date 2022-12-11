s=input()
cnt=0
for i in s:
    if i.isdigit():
        cnt+=1
if cnt>0:
    print("Contains",cnt,"digit")
else:
    print("Doesn't contain digit")