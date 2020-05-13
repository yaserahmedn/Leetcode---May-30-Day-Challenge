# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

# Example 1:

# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: [3,3,7,7,10,11,11]
# Output: 10
 

#O(N) solution
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        answer=0
        for num in nums:
            answer=answer^num
        return answer

#O(logN) solution - Source geeksforgeeks
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def binarySearch(left,right):
            if left>right:
                return None
            if left==right:
                return nums[left]
            
            mid=(left+right)//2
            
            if mid%2 == 0: 

                if nums[mid] == nums[mid+1]: 
                    return binarySearch(mid+2, right) 
                else: 
                    return binarySearch(left, mid) 

            else: 
                 
                if nums[mid] == nums[mid-1]: 
                    return binarySearch(mid+1, right) 
                else: 
                    return binarySearch(left, mid-1) 
        
        
        answer=binarySearch(0,len(nums)-1)
        return answer
