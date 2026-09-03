class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      digit_indexer={}
      index=0
      for num in nums:
        difference = target - num
        if difference not in digit_indexer:
            digit_indexer[num]=index
        else:
            return list((digit_indexer[difference],index))
        index+=1