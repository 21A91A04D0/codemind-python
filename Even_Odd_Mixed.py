def func(num):
    ec=0
    oc=0
    tc=0
    while num:
        d=num%10
        tc+=1
        if d%2==0:
            ec+=1
        elif d%2==1:
            oc+=1
        num=num//10
    if ec==tc:
        return "Even"
    elif oc==tc:
       return "Odd"
    else:
      return "Mixed"
num=int(input())
div=func(num)
print(div)