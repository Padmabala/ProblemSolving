listVowel=['a','e','i','o','u']
ch=input()
if(len(ch)>1):
    print("Enter a Character and not a string")
elif(ch in listVowel):
    print("Vowel")
elif((ch>='A'and ch<='Z') or (ch>='a'and ch<='z')):
    print("Consonant")
else:
    print("Enter a valid vowel or a consonent")