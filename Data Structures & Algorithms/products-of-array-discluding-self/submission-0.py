class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        count=[1]*len(nums)
        for index in range  (len(nums)):
            for idx in range (len(nums)):
                if idx!=index:
                    count[index]*=nums[idx]
        
        return (count)
            
            