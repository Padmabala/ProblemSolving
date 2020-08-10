n=input("Enter the no. of elements: ")
elements=[int(input()) for x in range(int(n))]
min=elements[0]
max=elements[0]
minIndex=0
maxIndex=0
for x in range(len(elements)):
    if(elements[x]<min):
        min=elements[x]
        minIndex=x
    elif(elements[x]>max):
        max=elements[x]
        maxIndex=x
print(min,' at ',minIndex,' and ',max,' at ',maxIndex)
