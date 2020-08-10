def findSum(lst,k):
    for i in range(len(lst)):
        temp=k-lst[i]
        s = set()
        flag = 0
        for j in range(i+1,len(lst)):
            pairSum = temp - lst[j]
            if pairSum in s:
                print(lst[j], pairSum,lst[i])
                flag = 1
            else:
                s.add(lst[j])

    if flag==0 :
        print("sum not found")

def findS(lst,k):
    s=set()
    flag=0
    for i in range(len(lst)):
        temp=k-lst[i]
        if temp in s:
            print(lst[i],temp)
            flag=1
            break
        else:
            s.add(lst[i])
    return flag
lst=[4,4,2,6,1]
findSum(lst,9)