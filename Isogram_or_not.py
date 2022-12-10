s=input()
d=list(s)
for i in d:
    if d.count(i)>1:
        print(False)
        break
else:
    print(True)