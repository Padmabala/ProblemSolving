def findImportance(lst):
    empDictionay={}
    for i in range(len(lst)):
        empDictionay[lst[i][0]]=lst[i]
    for i in range(len(lst)):
        sum = 0
        empList=lst[i]
        sum=sum+empList[1]
        for j in range(len(empList[2])):
            l1=empDictionay[empList[2][j]]
            sum=sum+l1[1]
        if(len(empList[2])==0):
            break
        else:
            print(sum)


lst=[[1,2,[2,3]],[2,3,[3]],[3,3,[]]]
findImportance(lst)