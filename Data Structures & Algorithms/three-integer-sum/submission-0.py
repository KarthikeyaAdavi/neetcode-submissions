class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        num_set=sorted(nums)
        print(num_set)
        for i in range (len(num_set)):
            left=i+1
            right=len(num_set)-1
            while left<right:
                if num_set[left]+num_set[right]>-num_set[i]:
                    right-=1
                elif num_set[left]+num_set[right]<-num_set[i]:
                    left+=1
                else:
                    if [num_set[left],num_set[right],num_set[i]] not in res:
                        res.append([num_set[left],num_set[right],num_set[i]])
                    left+=1
                    right-=1
        return res
            
                    
