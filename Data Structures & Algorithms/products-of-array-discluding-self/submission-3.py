class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums)
        for i,n in enumerate(nums):
            for idx,n in enumerate(nums):
                if idx!=i:
                    result[i]*=n
        return (result)
