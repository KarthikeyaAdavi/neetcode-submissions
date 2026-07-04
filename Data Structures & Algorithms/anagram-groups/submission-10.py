class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_list=defaultdict(list)
        for word in strs:
            count=[0]*26
            for char in word:
                count[ord(char)-ord('a')]+=1  
            anagrams_list[tuple(count)].append(word)
        return list(anagrams_list.values())

           
            
  