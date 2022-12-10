s=input()
v='aeiouAEIOU'
vc=0
c=0
d=0
w=0
for i in s:
    if i in v:
        vc+=1
    elif i not in v and i.isalpha():
        c+=1
    elif i.isdigit():
        d+=1
    elif i==' ':
        w+=1
print("Vowels:",vc)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)