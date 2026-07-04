class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count=[0]*26
        hashmap={}
        for string in strs:
            for char in string:
                count[ord(char)-ord('a')]+=1
            if tuple(count) not in hashmap:
                hashmap[tuple(count)]=[string]
            else:
                hashmap[tuple(count)].append(string)
            count=[0]*26
        return list(hashmap.values())
            