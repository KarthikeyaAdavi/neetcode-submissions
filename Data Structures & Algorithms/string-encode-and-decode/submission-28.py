class Solution:

    def encode(self, strs: List[str]) -> str:
            enc=''
            for word in strs:
                count=0
                for char in word:
                    count+=1
                enc+=str(count)+'#'+word
            print(enc)
            return enc

    def decode(self, s: str) -> List[str]:
            dec=[]
            i=0
            while i<len(s):
                length_of_word=''
                while '#'!=s[i]:
                    length_of_word+=s[i]
                    i+=1 #move ticker past i 
                i+=1 #move ticker past #
                length_of_word=int(length_of_word)
                dec.append(s[i:i+length_of_word])
                i+=length_of_word
            print(dec)
            return dec
            
            

