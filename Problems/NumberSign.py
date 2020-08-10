try:
    number=int(input())
    if(number+0>0):
        print("Positive")
    elif(number+0<0):
        print("Negative")
    else:
        print("Zero")
except:
    print("Enter a valid Integer")