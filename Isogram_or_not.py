s = input()
dic = {}
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for key, value in dic.items():
    if value != 1:
        print("False")
        break
else:
    print("True")