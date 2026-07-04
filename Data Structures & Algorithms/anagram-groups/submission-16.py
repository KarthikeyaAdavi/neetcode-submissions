class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_maps={}
        result=[]
        for word in strs:
            count=[0]*26
            for char in word:
                count[ord(char)-ord('a')]+=1
            if tuple(count) not in anagram_maps:
                anagram_maps[tuple(count)]=[word]
            else:
                anagram_maps[tuple(count)].append(word)
        result=list(anagram_maps.values())
        return result
