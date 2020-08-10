def getCoins(coins,t,i,j):
    result=[]
    while(j!=0):
        if(t[i][j]!=t[i-1][j]):
            result.append(coins[i-1])
            j=j-coins[i-1]
        else:
            i-=1
    return result
def getMinCoinsRequired(coins,n,total):
    t=[[float('inf') for j in range(total+1)]for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(total+1):
            if(j==0):
                t[i][j]=0
            elif(j<coins[i-1]):
                t[i][j] = t[i - 1][j]
            else:
                t[i][j] = min(t[i-1][j],1 + t[i][j - coins[i - 1]])
    result=getCoins(coins,t,n,total)
    return [t[n][total],result]
n=int(input("Enter the number of coins"))
coins=list(map(int,input().split(' ')[:n]))
total=int(input("Enter the sum"))
print(getMinCoinsRequired(coins,n,total))
