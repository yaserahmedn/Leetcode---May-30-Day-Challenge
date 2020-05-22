#Given a string, sort it in decreasing order based on the frequency of characters.
#
#Example 1:
#
#Input:
#"tree"
#
#Output:
#"eert"
#
#Explanation:
#'e' appears twice while 'r' and 't' both appear once.
#So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
#Example 2:
#
#Input:
#"cccaaa"
#
#Output:
#"cccaaa"
#
#Explanation:
#Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
#Note that "cacaca" is incorrect, as the same characters must be together.

class Solution:
    def frequencySort(self, s: str) -> str:
        d=dict()
        
        for char in s:
            d[char]=d.get(char,0)+1
            
        d=sorted(d.items(), key=lambda x:x[1], reverse=True)
        
        result=""
        
        for tuple in d:
            result+=tuple[0]*tuple[1]
            
        return result
