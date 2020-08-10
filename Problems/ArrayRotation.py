
def leftRotate(arr,n,d):
    if(d>n):
        d=d-n
    g=gcd(n,d)
    for i in range(g):
        temp=arr[i]
        j=i
        while 1:
            k=j+d
            if(k>=n):
                k=k-n
            if(k==i):
                break
            arr[j]=arr[k]
            j=k
        arr[j]=temp


def gcd(m,n):
    if(n==0):
        return m
    else:
        return gcd(n,n%m)
def leftRotateWithReversalAlgo(arr,n,d):
    temp=[]
    newArray=[]
    i=d-1
    while(i>=0):
        temp.append(arr[i])
        i=i-1
    print(temp)
    i=n-1
    while(i>=d):
        temp.append(arr[i])
        i=i-1
    print(temp)
    i=n-1
    while(i>=0):
        newArray.append(temp[i])
        i=i-1
    print(newArray)
arr=[1,2,3,4,5,6]
n=len(arr)
d=2

leftRotateWithReversalAlgo(arr,n,d)
print(arr)