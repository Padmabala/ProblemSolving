def tracepath(t,i,j,ip1,ip2):
    l=[]
    while True:
        if(t[i][j]!=t[i-1][j] and t[i][j]!=t[i][j-1]):
            l.append(ip1[i-1])
            i-=1
            j-=1
        else:
            if(i==0 or j==0):
                return l[::-1]
            if (t[i][j] == t[i - 1][j]):
                while(t[i][j]==t[i-1][j]):
                    i-=1
            elif(t[i][j] == t[i][j-1]):
                while(t[i][j] == t[i][j-1]):
                    j-=1


def LCS(ip1,ip2):
    l1=len(ip1)
    l2=len(ip2)
    t=[[0 for i in range(l2+1)]for j in range(l1+1)]
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if(ip1[i-1]==ip2[j-1]):
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])

    l=tracepath(t, i, j, ip1, ip2)
    # print(" ".join(l.reverse()))
    return [t[i][j],l]



ip1=input()
ip2=input()
print(LCS(ip1,ip2))