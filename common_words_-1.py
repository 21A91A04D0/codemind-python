a1=input()
a2=input()
s1=a1.lower()
s2=a2.lower()
d1=s1.split()
d2=s2.split()

d3=[]
cnt=0
for i in d1:
    if i in d2:
        d3.append(i)
for j in d2:
    if j in d1 and j not in d3:
        d3.append(j)
print(len(d3))
    