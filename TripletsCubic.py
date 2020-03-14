def tripletCubic(lst):

    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            for k in range(j+1,len(lst)):
                if(lst[i]+lst[j]+lst[k]==0):
                    lst1=[lst[i],lst[j],lst[k]]
                    print(lst1)


lst=[-1,0,1,2,-1,-4,2]
tripletCubic(lst)