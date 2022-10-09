num=int(input())
for i in range(1,num+1):
    a=i+1
    if i*a==num:
        print("YES")
        break
else:
    print("NO")