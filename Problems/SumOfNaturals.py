try:
    n=int(input())
    if(n<0):
        print("Enter a Positive Integer")
    else:
        sum=(n*(n+1))/2
        print(sum)
except:
    print("Enter a valid integer")