class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers={}
        for index,num in enumerate(nums):
            if num not in numbers.values():
                numbers[index]=num
            else:
                return True
        return False
        
        