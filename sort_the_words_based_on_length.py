def Sorting(lst):
    lst.sort(key=len)
    return lst
s=input()
lst=s.split()
s=Sorting(lst)
for i in range(len(s)-1):
    if len(s[i])==len(s[i+1]) and s[i]>s[i+1]:
        s[i],s[i+1]=s[i+1],s[i]
print(*s)