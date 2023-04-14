n = int(input())
num = list(str(n))
for i in range(len(num)):
    if num[i] == '6':
        num[i] = '9'
        break
print("".join(num))