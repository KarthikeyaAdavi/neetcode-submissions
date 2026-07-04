class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency={}
        for x in nums:
            frequency[x]=1+frequency.get(x,0)


        top=[]
        for num,cnt in frequency.items():
            top.append([cnt,num])
        top.sort()

        result=[]
        while len(result) < k:
            result.append(top.pop()[1])
        return result
        