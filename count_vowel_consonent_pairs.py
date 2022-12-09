s=input()
n=len(s)
i=0
j=n-1
cnt=0
vow='AEIOUaeiou'
while i<j:
    if s[i] in vow and s[j] not in vow and s[i]!=' ' and s[j]!=' ' or s[i] not in vow and s[j] in vow and s[i]!=' ' and s[j]!=' ':
        cnt+=1
    i+=1
    j-=1
print(cnt)