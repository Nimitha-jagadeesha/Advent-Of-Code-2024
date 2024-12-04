# Link: https://www.programiz.com/online-compiler/5zobXwLdR2ctT
n = 140
m = 140
arr = []
ans = 0
for i in range(0,n):
    arr = arr + [input()]
for i in range(0,n):
    for j in range(0,m):
        if(j+3<m and arr[i][j] == 'X' and arr[i][j+1] == 'M' and arr[i][j+2] == 'A' and arr[i][j+3] == 'S'):
            ans +=1
        if(i+3<n and arr[i][j] == 'X' and arr[i+1][j] == 'M' and arr[i+2][j] == 'A' and arr[i+3][j] == 'S'):
            ans +=1
        if(i-3>=0 and arr[i][j] == 'X' and arr[i-1][j] == 'M' and arr[i-2][j] == 'A' and arr[i-3][j] == 'S'):
            ans +=1
        if(j-3>=0 and arr[i][j] == 'X' and arr[i][j-1] == 'M' and arr[i][j-2] == 'A' and arr[i][j-3] == 'S'):
            ans +=1
        if(i-3>=0 and j-3 >=0 and arr[i][j] == 'X' and arr[i-1][j-1] == 'M' and arr[i-2][j-2] == 'A' and arr[i-3][j-3] == 'S'):
            ans +=1
        if(i+3<n  and j+3<m and arr[i][j] == 'X' and arr[i+1][j+1] == 'M' and arr[i+2][j+2] == 'A' and arr[i+3][j+3] == 'S'):
            ans +=1
        if(i+3<n  and j-3>=0 and arr[i][j] == 'X' and arr[i+1][j-1] == 'M' and arr[i+2][j-2] == 'A' and arr[i+3][j-3] == 'S'):
            ans +=1
        if(i-3>=0  and j+3<m and arr[i][j] == 'X' and arr[i-1][j+1] == 'M' and arr[i-2][j+2] == 'A' and arr[i-3][j+3] == 'S'):
            ans +=1
        
print(ans)
