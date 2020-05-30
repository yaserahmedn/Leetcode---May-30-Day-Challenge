'''
  Counting Bits
Solution
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
'''

class Solution:
    def countBits(self, num: int) -> List[int]:
        result=[]
        for number in range(0,num+1):
            binary = bin(number).replace('0b','')
            #print(binary)
            count=binary.count('1')
            result.append(count)
            
        return result
