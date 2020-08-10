n=int(input())
vowels=['a','e','i','o','u','A','E','I','O','U']
for _ in range(n):
    s = input()
    cnt=0
    for j in range(len(s)):
         if(s[j] in vowels):
                cnt += (len(s)-j)*(j+1)
    print(cnt)
# def substring(s,vowels):
#     l=[]
#     substringSum=0
#     sum=0
#     for i in range(len(s)):
#         substringSum=0
#         tmp=s[i]
#         l.append(tmp)
#         if(s[i] in vowels):
#             substringSum+=1
#             sum=sum+substringSum
#         for j in range(i+1,len(s)):
#             tmp=tmp+s[j]
#             if(s[j] in vowels):
#                 substringSum+=1
#             sum=sum+substringSum
#     return sum
#
# while True:
#     vowels=['a','e','i','o','u','A','E','I','O','U']
#     try:
#         t=int(input())
#         s=[input() for i in range(t)]
#         for i in range(len(s)):
#             print(substring(s[i],vowels))
#     except EOFError:
#         break