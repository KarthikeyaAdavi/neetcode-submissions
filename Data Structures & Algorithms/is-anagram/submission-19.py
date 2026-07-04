class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count=[0]*26
        for index in range (len(s)):
            count[ord(s[index])-ord('a')]+=1
            count[ord(t[index])-ord('a')]-=1
        for c in count:
            if c != 0:
                return False
        return True

        
            
