
def main():
    list2=["abc","def","ghi"]
    len1=len(list2)
    for i in range(0,len1):
        list2[i].capitalize()
        print(list2[i])
    print(list2)
if(__name__=="__main__"):
    main()