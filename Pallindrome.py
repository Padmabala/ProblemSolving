n=input()
sum=0
for i in range(len(n)):
    sum=sum+int(n[i])
sum=str(sum)
i=0
j=len(sum)-1

flag=False
if(i==j):
    flag=True
else:
    while(i!=j and i<j):
        if(sum[i]==sum[j]):
            flag=True
        else:
            flag=False
            break
        i+=1
        j-=1
if(flag==False):
    print("No")
else:
    print("Yes")