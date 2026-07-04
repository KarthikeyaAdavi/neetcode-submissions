class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         dicti=set()
         for x in nums:
            if x not in dicti:
                dicti.add(x)
            else:
                 return True
         return False