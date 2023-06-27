r,c = map(int, input().split())
row = [0 for i in range(c)]
d = [row.copy() for i in range(r)]
for i in range(r):
    val = list(map(int,input().split()))
    for j in range(c):
        d[i][j] = val[j] 
lst1 = [0 for i in range(r)]
lst2 = [0 for i in range(c)]
for i in range(r):
    for j in range(c):
        lst1[i] += d[i][j]
        lst2[j] += d[i][j]
print(max(max(lst1),max(lst2)))