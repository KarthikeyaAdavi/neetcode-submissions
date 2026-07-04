class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        wordcounts={}
        wordcountt={}
        for i in range(len(s)):
            if s[i] not in wordcounts:
                wordcounts[s[i]]=1
            else:
                wordcounts[s[i]]+=1  
            if t[i] not in wordcountt:
                wordcountt[t[i]]=1
            else:
                wordcountt[t[i]]+=1
        if wordcounts == wordcountt:
            return True
        else:
            return False