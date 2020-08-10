def knapSack(itemList,total):
    t=[[' ' for i in range(total+1)]for j in range(len(itemList)+1)]
    for i in range(len(itemList)+1):
        for j in range(0,total+1):
            if(i==0 or j==0):
                t[i][j]=0
                continue
            item = itemList[i - 1]
            wt=j
            if(wt-item.wt>=0):
                t[i][j] = max(t[i - 1][j], item.val + t[i - 1][(wt - item.wt)])
            else:
                t[i][j]=t[i-1][j]

    l=tracePath(i,j,t,itemList)
    return[t[i][j],l]

    # print("hello")
def tracePath(i,j,t,itemList):
    wt=[]
    val=[]
    while(True):
        if(t[i][j]==0):
            return [wt,val]
        if (t[i][j]==t[i - 1][j]):
            i=i-1
        else:
            wt.append(itemList[i-1].wt)
            val.append(itemList[i-1].val)
            j = j - itemList[i - 1].wt
            i -= 1
class items:
    def __init__(self,wt,val):
        self.wt=wt
        self.val=val

n=int(input())
itemList=[]
print("Enter weight and val of the item separated by space")
for i in range(n):
    wt,val=map(int,input().split())
    item=items(wt,val)
    itemList.append(item)
# print(itemList)

total=int(input("Enter the total Weight"))

print(knapSack(itemList,total))

