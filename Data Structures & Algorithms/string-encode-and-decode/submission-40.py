class Solution:

    def encode(self, strs: List[str]) -> str:
        count=0
        enc=''
        for word in strs:
            for char in word:
                count+=1
            enc=enc+str(count)+'#'+word
            count=0
        print(enc)
        return enc

    def decode(self, s: str) -> List[str]:
        dec=[]
        idx=0
        length=''
        while (idx<len(s)):
            while s[idx]!='#':
                length+=s[idx]
                idx+=1
            idx+=1
            word=s[idx:idx+int(length)]
            idx=idx+int(length)
            length=''
            dec.append(word)
        return dec
            






            
            

