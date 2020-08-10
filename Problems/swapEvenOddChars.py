str1=input()
s=list(str1)
for i in range(1,len(s),2):
	temp=s[i-1]
	s[i-1]=s[i]
	s[i]=temp

str1=''.join([str(elem) for elem in s])
a=str1.strip()
print(a)