def count(ch):
    vowels='aeiouAEIOU'
    z=[]
    if ch[0] in vowels and ch[-1] not in vowels:
        z.append(ch)
    return z
s=input()
k=s.split()
cnt=0
for i in k:
    if count(i):
        cnt+=1
print(cnt)
    
    
    