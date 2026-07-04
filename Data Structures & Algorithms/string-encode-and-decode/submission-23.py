class Solution:

    def encode(self, strs: List[str]) -> str:
            enc=''
            no_of_words=0
            for word in strs:
                count=0
                for ch in word:
                    count+=1
                enc+= str(count)+'#'+word
                no_of_words+=1
            return enc

    def decode(self, s: str) -> List[str]:
            dec=[]
            i=0
            while i < len(s):
                length_of_word=''
                while s[i]!='#':
                    length_of_word+=s[i]
                    i+=1
                length_of_word=int(length_of_word)
                i+=1
                word=s[i:i+length_of_word]
                dec.append(word)
                i+=length_of_word
            return dec

            
            

