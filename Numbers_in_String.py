s=input()
k=[]
for i in s:
    if i.isdigit():
        k.append(int(i))
print(sum(k))