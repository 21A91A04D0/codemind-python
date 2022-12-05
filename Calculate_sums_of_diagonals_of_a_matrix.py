n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

c=0
right=0
left=0
j=0
for i in range(0,n):
    right+=arr[i][i]
    
    left+=arr[j][n-j-1]
    
    if arr[i][i]==arr[j][n-j-1]:
        c=arr[j][n-j-1]
    j+=1
print(right+left-c)