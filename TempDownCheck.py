def checkTemp(lst):
    sorted=(list(set(lst)))
    d={}
    for i in range(len(lst)):
        if lst[i] in d:
            t=d[lst[i]]
            t.append(i)
            d[lst[i]]=t
        else:
            d[lst[i]]=[i]

    print(sorted)
    for i in range(len(lst)):
        h=findElement(sorted,0,len(sorted),lst[i])
        print(h)
        i=sorted[h:]
        print("list is ", i,"\n")


def findElement(arr, l, r, k):
    #print(l,r)
    if (l <= r):
        mid = int((l + (r)) / 2)
        if (arr[mid]==k):
            return mid
        elif (k < arr[mid]):
            findElement(arr, l, mid - 1, k)
        else:
            findElement(arr, mid + 1, r, k)


lst=[73,74,75,71,69,72,76,73]
#[1,1,4,,2,1,
checkTemp(lst)