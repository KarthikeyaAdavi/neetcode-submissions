class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ltr_cnt={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            ltr_cnt[s[i]]=ltr_cnt.get(s[i],0)+1
            ltr_cnt[t[i]]=ltr_cnt.get(t[i],0)-1
        print(ltr_cnt)
        for num in ltr_cnt.values():
            if num!=0:
                return False
        return True

            