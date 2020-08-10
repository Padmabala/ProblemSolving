def trace(arr,total,t,i,j):
    result=[]
    while(j!=0):
        if(t[i][j]==t[i-1][j]):
            i-=1
        else:
            result.append(arr[i-1])
            j = j - arr[i - 1]
            i-=1
    return result

def subsetSum(arr,n,total):
    t=[[' ' for j in range(total+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(total+1):
            if(j==0):
                t[i][j]=True
            elif(i==0):
                t[i][j]=False
            else:
                remainingSum=j-arr[i-1]
                if(remainingSum>=0):
                    t[i][j] = t[i - 1][j] or t[i - 1][remainingSum]
                else:
                    t[i][j] = t[i - 1][j]
    result=trace(arr,total,t,i,j)
    return [t[n][total],result]



n=int(input("Entert the value of n"))
arr=list(map(int,input().split(' ')[:n]))
total=int(input("Enter the Total"))
print(subsetSum(arr,n,total))