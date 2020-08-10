def buildSequence(array,sequence,currIndex):
    s=[]
    while(currIndex is not None):
        s.append(array[currIndex])
        currIndex=sequence[currIndex]
    return list(reversed(s))
def longestIncreasingSubsequence(array):
    m=[1 for _ in range(len(array))]
    j=0
    i=j+1
    sequences=[None for x in array]
    maxIndex=0
    while(j<len(array)-1):
        if(i==j):
            j=0
            i+=1
        else:
            if(array[i]>array[j]):
                if(m[j]+1>m[i]):
                    m[i]=m[j]+1
                    sequences[i]=j
            if(m[i]>=m[maxIndex]):
                maxIndex=i
            j+=1
    return buildSequence(array, sequences, maxIndex)
n=int(input())
array=list(map(int,input().split(' ')[:n]))
print(longestIncreasingSubsequence(array))