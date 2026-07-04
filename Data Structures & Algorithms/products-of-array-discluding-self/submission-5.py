class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt,prod=0,1
        for num in nums:
            if num:
                prod*=num
            else:
                zero_cnt+=1
        
        if zero_cnt>1:return [0]*len(nums)
        result=[1]*len(nums)
        for i,c in enumerate(nums):
            if zero_cnt:result[i]=0 if c else prod
            else:
                result[i]=prod//c
        return result