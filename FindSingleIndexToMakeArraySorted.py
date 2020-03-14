n=int(input())
lst=list(map(int,input().split()[:n]))
lstLength=len(lst)-1
index=-1
found=False
for i in range(n-1):
    if(lst[i]>lst[i+1]):
        if(found==False):
            index=i
            found=True
        else:
            index=-1
            break
print(index)