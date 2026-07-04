class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers={}
        for index,num in enumerate(nums):
            if num in numbers.values():
                return True
            else:
                numbers[index]=num
                
        return False
        
        