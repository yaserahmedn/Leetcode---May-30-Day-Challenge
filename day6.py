class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold=len(nums)//2
        
        for digit in set(nums):
            if nums.count(digit)>threshold:
                return digit
        
