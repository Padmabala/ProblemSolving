def equalPartitions(n,arr):
    sum=0
    for i in arr:
        sum+=i
    if(sum%2!=0):
        return False
    sum=sum//2
    t=[[' ' for j in range(sum+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(sum+1):
            if(j==0):
                t[i][j]=True
            elif(i==0):
                t[i][j]=False
            else:
                remainingSum=j-arr[i-1]
                if(remainingSum>=0):
                    t[i][j] = t[i - 1][j] or t[i - 1][remainingSum]
                else:
                    t[i][j]=t[i-1][j]
    print(t)
    return t[n][sum]
n=int(input())
arr=list(map(int,input().split(' ')[:n]))
print(equalPartitions(n,arr))