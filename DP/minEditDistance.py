def tracePath(ip1,ip2,t,i,j):
    result=""
    while(i>0):
        if(ip1[i-1]!=ip2[j-1]):
            if(t[i][j]==t[i-1][j-1]+1):
                result=result+"convert "+ip2[j-1]+"->"+ip1[i-1]+","
                i=i-1
                j=j-1
            elif(t[i][j]==t[i][j-1]+1):
                result=result+"delete "+ip2[j-1]+","
                j=j-1
            elif(t[i][j]==t[i-1][j]+1):
                result=result+"add "+ip1[i-1]+","
                i=i-1
        else:
            result=result+ip1[i-1]+","
            i-=1
            j-=1
    edits=result.split(',')
    edits.reverse()
    return edits


def minEditDistance(ip1,ip2):
    t=[[float('inf') for j in range(len(ip2)+1)]for i in range(len(ip1)+1)]
    for i in range(len(ip1)+1):
        for j in range(len(ip2)+1):
            if(i==0):
                t[i][j]=j
                continue
            elif(j==0):
                t[i][j]=i
                continue
            if(ip1[i-1]==ip2[j-1]):
                t[i][j]=t[i-1][j-1]
            else:
                t[i][j]=min(
                    t[i-1][j],
                    t[i][j-1],
                    t[i-1][j-1])+1
    result=tracePath(ip1,ip2,t,i,j)
    return [t[i][j],result[1:]]
ip1=input()
ip2=input()
print(minEditDistance(ip1,ip2))