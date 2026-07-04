class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        wordcounts={}
        wordcountt={}
        for i in s:
            if i not in wordcounts:
                wordcounts[i]=1
            else:
                wordcounts[i]+=1
        for i in t:     
            if i not in wordcountt:
                wordcountt[i]=1
            else:
                wordcountt[i]+=1
        if wordcounts == wordcountt:
            return True
        else:
            return False