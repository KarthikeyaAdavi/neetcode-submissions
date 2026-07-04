class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        count=[1]*n
        for index in range  (n):
            for idx in range (n):
                if idx!=index:
                    count[index]*=nums[idx]
        
        return (count)
            
            