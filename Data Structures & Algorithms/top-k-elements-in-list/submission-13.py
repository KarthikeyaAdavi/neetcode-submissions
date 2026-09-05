class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_counter={}
        res=[]
        frequency=[[] for i in range(len(nums)+1)]
        for num in nums:
            number_counter[num]=1+number_counter.get(num,0)
        for  n , c in number_counter.items():
            frequency[c].append(n)
        for i in range(len(frequency)-1,0,-1):
            for num in frequency[i]:
                res.append(num)
            if len(res)==k:
                break
        return res