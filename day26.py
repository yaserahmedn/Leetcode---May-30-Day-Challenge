#Contiguous Array
#Solution
#Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

#Example 1:
#Input: [0,1]
#Output: 2
#Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
#Example 2:
#Input: [0,1,0]
#Output: 2
#Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#Note: The length of the given binary array will not exceed 50,000.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        base_count=dict()
        base_count[0]=-1
        count=0
        max_length=0
        n=len(nums)
        for i in range(0,n):
            if nums[i]==0:
                count=count-1
            else:
                count=count+1
                
            if count not in base_count:
                base_count[count]=i
            else:
                max_length=max(max_length, i-base_count[count])
                
        return max_length
