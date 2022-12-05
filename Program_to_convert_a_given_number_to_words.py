n=int(input())
ones={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
tens={10:'ten',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
u_tens={11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'ninteen'}
temp=str(n)
l=len(temp)
k=n
a=1000
d=0
if n==0:
    print("zero")
if n<10 and n>0:
    print(ones[n],end=' ')
if l==4:
    a=1000
    while n:
        d=n%a
        f=n//a
        if f in ones:
            print(ones[f],"thousand",end=' ')
            break
elif l==3:
    a=a//10
    while k:
        k_1=k%a#1
        f_5=k//a#5
        
        if f_5 in ones:
            print(ones[f_5],"hundred",end=' ')
            break
    if k_1<10 and k_1>0:
        print(ones[k_1],end=' ')
            
    string=str(k_1)
    if len(string)==2 and k_1 in tens:
        print(tens[k_1],end=' ')
        
    elif len(string)==2 and k_1 in u_tens:
        print(u_tens[k_1],end=' ')
    elif len(string)==2:
        d_units=k_1//10
        d_k=k_1%10
        a_d=d_units*10
        if a_d in tens:
            print(tens[a_d],end=' ')

        if d_k in ones:
            print(ones[d_k],end=' ')
elif l==2:
    a=a//100
    if k in tens:
        print(tens[k],end=' ')
    elif k in u_tens:
        print(u_tens[k],end=' ')
    elif k>20 and k<100:
        d_dd=k%10#3
    
        d_uu=k//10#2
        d_pow=d_uu*10#
        print(tens[d_pow]+" "+ones[d_dd])
    
        
temp_1=str(d)
l_1=len(temp_1)
if l_1==3:
    a=a//10
    while d:
        d_1=d%a
        f_1=d//a
        if f_1 in ones:
            print(ones[f_1],"hundred",end=' ')
            break
elif l_1==2:
    while d:
        f_1=d//10
        d_1=d%10
        power=f_1*10
        if power in tens:
            print(tens[power],end=' ')
            break
    if d_1 in ones:
        print(ones[d_1],end=' ')
elif l_1==1:
    d_1=d
    if d in ones:
        print(ones[d],end=' ')
temp_2=str(d_1)
l_2=len(temp_2)
if l_2==2:
    a=a//10
    while d_1:
        val_d=d_1//10
        digit=d_1%10
        power=val_d*10
        if power in tens:
            print(tens[power],end=' ')
            break
    if digit in ones:
        print(ones[digit],end=' ')
elif l_2==2:
    a=a//10
if d_1 in tens:
    print(tens[d_1],end=' ')
elif d_1 in u_tens:
    print(u_tens[d_1],end=' ')
