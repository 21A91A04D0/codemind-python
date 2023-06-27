r,c = map(int, input().split())
row = [0 for i in range(c)]
d = [row.copy() for j in range(r)]
for i in range(r):
    val = list(map(int,input().split()))
    for j in range(c):
        d[i][j] = val[j]
sm = 0
for i in range(r):
    for j in range(c):
        if i == 0 or i == r - 1 or j == 0 or j == c - 1:
            sm += d[i][j]
print(sm)