n=int(input())
k=int(input())
list1=[]
sum1=0
print("Enter ",n," List Elements:")
for i in range(0,n):
    list1.append(int(input()))
for j in range(0,k):
    sum1=sum1+list1[j]
print("Sum is ",sum1)