def buildSequence(array,sequence,currIndex):
    s=[]
    while(currIndex is not None):
        s.append(array[currIndex])
        currIndex=sequence[currIndex]
    return list(reversed(s))
def bsearch(start,end,indices,array,key):
    if(start>end):
        return start
    middle=(start+end)//2
    if(key>array[indices[middle]]):
        start=middle+1
    else:
        end=middle-1
    return bsearch(start, end, indices, array, key)

def LongestIncreasingSubsequence(array):
    length=0
    sequences=[None for x in array]
    indices=[None for i in range(len(array)+1)]
    for i,num in enumerate(array):
        newLength=bsearch(1, length, indices, array, num)
        sequences[i]=indices[newLength-1]
        indices[newLength]=i
        length=max(length,newLength)
    return buildSequence(array,sequences,indices[length])
n=int(input())
a=list(map(int,input().split(' ')[:n]))
print(LongestIncreasingSubsequence(a))