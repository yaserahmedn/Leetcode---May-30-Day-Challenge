#Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

#Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

#The order of output does not matter.

#Example 1:

#Input:
#s: "cbaebabacd" p: "abc"

#Output:
#[0, 6]

#Explanation:
#The substring with start index = 0 is "cba", which is an anagram of "abc".
#The substring with start index = 6 is "bac", which is an anagram of "abc".


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result=[]
        
        countp=Counter(p)
        #print(countp)
        lengthp=len(p)
        traversal=len(s)-lengthp+1
        i=0
        
        while(i<traversal):
            
            if Counter(s[i:i+lengthp])==countp:
                result.append(i)
            i=i+1
            
        return result
