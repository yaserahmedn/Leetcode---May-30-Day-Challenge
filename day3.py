class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_set=set(ransomNote)
        
        flag=True
        for i in ransom_set:
            if ransomNote.count(i)> magazine.count(i):
                flag=False
                break
        return flag
