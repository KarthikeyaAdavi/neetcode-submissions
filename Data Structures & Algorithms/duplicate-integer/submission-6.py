class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers={}
        for index,num in enumerate(nums):
            if num in numbers:
                return True
            else:
                numbers[num]=index
                
        return False
        
        