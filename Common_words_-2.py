a1=input()
a2=input()
s1=a1.lower()
s2=a2.lower()
d1=s1.split()
d2=s2.split()

d3=[]
cnt=0
for i in d1:
    if i in d2 and d2.count(i)==1 and d1.count(i)==1:
        d3.append(i)
print(len(d3))
    