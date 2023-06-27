def fun(lst):
    k = lst.copy()
    k1 = lst.copy()
    lst.sort()
    k1.sort(reverse = True)
    if lst == k or k1 == k:
        return True
    return False
r,c = map(int, input().split())
row = [0 for i in range(c)]
d = [row.copy() for j in range(r)]
for i in range(r):
    val = list(map(int,input().split()))
    for j in range(c):
        d[i][j] = val[j]
rs = [[] for i in range(r)]
cnt = 0
for i in range(r):
    for j in range(c):
        rs[i].append(d[i][j])
for k in rs:
    if fun(k):
        cnt += 1
print(cnt)