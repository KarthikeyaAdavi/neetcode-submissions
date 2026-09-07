class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        result=[]
        zero_cnt=0
        for i in range(len(nums)):
            if nums[i]!=0:
                product*=nums[i]
            else:
                zero_cnt+=1
        if zero_cnt>1:
            return [0]*len(nums)
        elif zero_cnt==1:
            for i in range (len(nums)):
                if nums[i]==0:
                    result.append(product)
                else:
                    result.append(0)
        else:
            for i in range(len(nums)):
                result.append(int(product/nums[i]))

        return result

   

