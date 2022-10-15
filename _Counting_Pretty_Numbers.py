for i in range(int(input())):
    l,r=map(int,input().split())
    p=0
    for i in range(l,r+1):
        d=i%10
        if d==2 or d==3 or d==9:
            p+=1
    print(p)