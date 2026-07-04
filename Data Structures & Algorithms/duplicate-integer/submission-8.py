class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp=0
        duplicate_map={}
        for i,n in enumerate(nums):
            if n not in duplicate_map.keys():
                duplicate_map[n]=i
            else:
                return True

            print(duplicate_map)
        return False
