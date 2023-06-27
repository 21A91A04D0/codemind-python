def fun(lst):
    k = lst.copy()
    lst.sort()
    if k == lst:
        return True
    return False
r,c = map(int, input().split())
row = [0 for i in range(c)]
d = [row.copy() for j in range(r)]
for i in range(r):
    val = list(map(int,input().split()))
    for j in range(c):
        d[i][j] = val[j]
rs = [0 for i in range(r)]
cs = [[] for i in range(c)]
cnt = 0
for i in range(r):
    for j in range(c):
        cs[j].append(d[i][j])
for k in cs:
    if fun(k):
        cnt += 1
print(cnt)