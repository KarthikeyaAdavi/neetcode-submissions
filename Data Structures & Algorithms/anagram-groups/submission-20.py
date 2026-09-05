class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        mapper={}
        for i in range(len(strs)):
            count=[0]*26
            for char in strs[i]:
                count[ord(char)-ord('a')]+=1
            if tuple(count) not in mapper:
                mapper[tuple(count)]=[strs[i]]
            else:
                mapper[tuple(count)].append(strs[i])

        result=mapper.values()
        return list(result)