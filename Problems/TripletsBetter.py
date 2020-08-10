def tripletSum(lst,sum):
    n=len(lst)
    uniqueSet=set()
    for i in range(n-2):
        pairSum=sum-lst[i]
        s=set()
        flag=0
        for j in range(n):
            temp=pairSum-lst[j]
            if temp in s:
                uniqueSet.add((lst[i],lst[j],temp))
                flag=1
                break
            else:
                s.add(lst[j])
    if(flag==0):
        print("Triplet Not Found")
    print("Triplet that sum to 0 is : ",uniqueSet)

n=int(input("Enter the size of the list"))
print("Enter the Numbers separated by line")
lst=list(map(int,input().split()[:n]))

#lst=[-1,0,1,2,-1,-4,2]
tripletSum(lst,0)