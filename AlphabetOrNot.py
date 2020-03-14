stre=input("Enter a Character: ")
for ch in stre:
    if((ch>='A'and ch<='Z') or (ch>='a'and ch<='z')):
        flag=0
    else:
        flag=1
        break
if(flag==0):
    print("Alphabet")
else:
    print("No")