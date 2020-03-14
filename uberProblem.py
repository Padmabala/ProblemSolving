def calculateTravelCost(a,b,perKmCost):
    dist=locB-locA
    cost=perKmCost*dist
    print(cost)
def checkCabAvailabilityAndGetPerKMCost(cabType,totalMiniCabs,totalMacroCabs,totalPrimeCabs,BookedMiniCab,BookedMacroCab,BookedPrimeCab):
    if (cabType == 1):
        BookedMiniCab+=1
        print("BMC",BookedMiniCab)
        print("Total")
        if(BookedMiniCab<=totalMiniCabs):
            perKmCost = 5
        else:
            print("Sorry no cabs available! Choose any other CabType")
            perKmCost = -1
    elif (cabType == 2):
        BookedMacroCab += 1
        if (BookedMacroCab <= totalMacroCabs):
            perKmCost = 10
        else:
            print("Sorry no cabs available! Choose any other CabType")
            perKmCost = -1
    elif (cabType == 3):
        BookedPrimeCab += 1
        if (BookedPrimeCab <= totalPrimeCabs):
            perKmCost = 15
            return perKmCost
        else:
            print("Sorry no cabs available! Choose any other CabType")
            perKmCost = -1
    else:
        print("Invalid CabTypes.Please Choose from the list")
        perKmCost = -1
    return perKmCost

totalMiniCabs = int(input("Total No. of Mini cabs"))
totalMacroCabs = int(input("Total No. of Macro cabs"))
totalPrimeCabs = int(input("Total No. of Prime cabs"))
BookedMiniCab = 0
BookedMacroCab = 0
BookedPrimeCab = 0
bookCab="y"
perKmCost=0
while(bookCab=="y" and perKmCost>=0):
    locA = int(input("Source"))
    locB = int(input("Target"))
    cabType = int(input("Available Cabs are: \n1.Mini\n2.Macro\n3.Prime"))
    perKmCost=checkCabAvailabilityAndGetPerKMCost(cabType,totalMiniCabs,totalMacroCabs,totalPrimeCabs,BookedMiniCab,BookedMacroCab,BookedPrimeCab)
    if(perKmCost>0):
        calculateTravelCost(locA, locB, perKmCost)
        bookCab = input("Do u wanna book another cab?y/n")
print("Thank You for using uber")

