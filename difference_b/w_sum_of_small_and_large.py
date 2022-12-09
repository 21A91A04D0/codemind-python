s=input()
k=s.split()
mini=[]
maxi=[]
mins=0
maxs=0
for i in k:
    mini.append(min(i))
    maxi.append(max(i))
for i in mini:
    mins+=ord(i)
for i in maxi:
    maxs+=ord(i)
print(abs(mins-maxs))
    