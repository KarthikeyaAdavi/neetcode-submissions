class Solution:
    def isPalindrome(self, s: str) -> bool:
        text=''
        inp=s.lower()
        for i in range(len(inp)):
            if 'a'<=inp[i]<='z' or '0'<=inp[i]<='9' or 'A'<=inp[i]<='Z':
                text+=inp[i]
            else:
                pass
        l=0
        r=-1
        while l <= len(text)+r:
            if text[l]!=text[r]:
                return False
            l+=1
            r-=1
        return True