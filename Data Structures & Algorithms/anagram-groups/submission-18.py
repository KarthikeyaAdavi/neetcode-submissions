class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=dict()
        for word in strs:
            count=[0]*26
            for char in word:
                count[ord(char)-ord('a')]+= 1
            if tuple(count) not in result.keys():
                result[tuple(count)]=[word]
            else:
                result[tuple(count)]+=[word]
        return list(result.values())