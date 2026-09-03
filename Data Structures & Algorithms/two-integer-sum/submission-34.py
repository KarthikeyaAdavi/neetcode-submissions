class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper={}
        index=0
        for num in nums:
            difference=target-num
            if difference not in mapper:
                mapper[num]=index
            else:
                return list((mapper[difference],index))

            index+=1