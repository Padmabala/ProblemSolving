try:
    number=int(input())
    if(number<0):
        print("Enter a positive number")
    elif(number%2==0):
        print("Even")
    else:
        print("Odd")
except:
    print("Enter a valid type of data")