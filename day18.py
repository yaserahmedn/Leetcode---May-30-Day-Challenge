#Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

#Example 1:

#Input: s1 = "ab" s2 = "eidbaooo"
#Output: True
#Explanation: s2 contains one permutation of s1 ("ba").
#Example 2:

#Input:s1= "ab" s2 = "eidboaoo"
#Output: False
 

#Note:

#The input strings only contain lower case letters.
#The length of both given strings is in range [1, 10,000].


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window=len(s1)
        
        sets1=set(s1)

        count=[0] * 26

        for ch in s1:
            count[ord(ch) - ord('a')]+=1
    
        traversal=len(s2)-window
        
        for i in range(traversal+1):
            compareStr=s2[i:i+window]
            setCompareStr=set(compareStr)
            counter=0
            if len(sets1)==len(setCompareStr):
                for ch in setCompareStr:
                    if compareStr.count(ch)==count[ord(ch)-97]:
                        counter+=1
                        
            if counter==len(sets1):
                return True
                
        return False
            
