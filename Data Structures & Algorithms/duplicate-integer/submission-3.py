class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         number_tracker={}
         for i in range(len(nums)):
             if nums[i] not in number_tracker:
                number_tracker[nums[i]]=i
             else: 
                return True
         return False