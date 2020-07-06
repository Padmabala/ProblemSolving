class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magList = list(magazine)
        magHash = {}
        for i in range(len(magList)):
            if magList[i] not in magHash:
                magHash[magList[i]] = 1
            else:
                magHash[magList[i]] += 1
        ransomNoteList = list(ransomNote)
        for i in range(len(ransomNoteList)):
            if ransomNoteList[i] not in magHash or magHash[ransomNoteList[i]]==0:
                return False
            else:
                if (magHash[ransomNoteList[i]] >= 1):
                    magHash[ransomNoteList[i]] -= 1
        return True

s=Solution()
print(s.canConstruct("aa","ab"))
