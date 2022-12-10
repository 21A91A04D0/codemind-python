for _ in range(int(input())):
    s=input()
    for i in s:
        if i.isdigit():
            print("Yes")
            break
    else:
        print("No")