def vowel_count(ch):
    vow='aeiouAeiou'
    cnt=0
    for i in ch:
        if i in vow:
            cnt+=1
    return cnt
            
s=input()
k=s.split()
d=list(k)
a=[]
for i in d:
    if vowel_count(i):
        a.append(vowel_count(i))
print(*a)
        
    