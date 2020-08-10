#python code goes here
#python version :3

def convert(s):
    if(len(s)==0):
        "Empty String"
    s1=''
    s1+=s[0].upper()
    len1=len(s)
    for i in range(1,len1-1):
        if(s[i]==' '):
            s1+=s[i+1].upper()
            i+=1
        elif(s[i-1]!=' '):
            s1+=s[i]
        else:
            i+=1
    print(s1)

def main():
    s="i am an intern at geeks for geeks"
    convert(s)
if(__name__=="__main__"):
    main()