class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max=0
        j=0
        str=[]
        count=0
        for i in range(len(s)):
            if s[i] not in str:
                str.append(s[i])
                count+=1
            else:
                while(True):
                    while (str[j] != s[i]):
                        j += 1
                        count -= 1
                    count -= 1
                    j+=1
                    str = str[j:]
                    if s[i] not in str:
                        str.append(s[i])
                        count += 1
                        j = 0
                        break

            if(count>max):
                max=count
        return max

s=Solution()
print(s.lengthOfLongestSubstring("dvdf"))

