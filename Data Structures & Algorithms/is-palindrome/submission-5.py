class Solution:
    def isPalindrome(self, s: str) -> bool:
        strn=''
        inp=s.lower()
        l=0
        r=-1
        if len(inp)==1:
            return True

        for i in range(len(s)):
            if 'a'<=inp[i]<='z' or '0'<=inp[i]<='9' or 'A'<=inp[i]<='Z':
                strn+=inp[i]

        if len(strn)==1 or strn=='':
            return True
        while l<=len(s)+r:
            if strn[l]!=strn[r]:
                return False
            l+=1
            r-=1
        return True
            
            
