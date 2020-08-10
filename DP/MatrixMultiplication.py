def multiplyMatrices(matrices,n):
    t=[[0 for i in range(n)]for j in range(n)]
    q=0
    for i in range(1,n):
        t[i][i]=0
    for l in range(2,n+1):
        for i in range(n-l+1):
            j=i+l-1
            t[i][j]=float('inf')
            for k in range(i,j):
                q=t[i][k]+t[k+1][j]+matrices[i][0]*matrices[k][1]*matrices[j][1]
                if(q<t[i][j]):
                    t[i][j]=q
    return t[0][n-1]



n=int(input("Enter the number of matrices"))
print("Enter in new line ",n,"matrice dimension(x,y) separated by space")
matrices=list(list(map(int,input().split(' ')))for i in range(4))
# matrices = [[2,3],[3,6],[6,4],[4,5]];
print(multiplyMatrices(matrices,4))