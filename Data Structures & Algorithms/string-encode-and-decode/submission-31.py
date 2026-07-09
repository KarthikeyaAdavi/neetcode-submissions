class Solution:

    def encode(self, strs: List[str]) -> str:
            enc=''
            for i in range (len(strs)):
                length_of_word=0
                for j in range(len(strs[i])):
                    length_of_word+=1
                enc+=str(length_of_word)+'#'+strs[i]
            return enc


    def decode(self, s: str) -> List[str]:
        dec=[]
        i=0
        print(s)
        while i < len(s):
            word=''
            length_of_word=''
            while s[i]!='#':
                length_of_word+=s[i]
                i+=1
            i+=1
            length_of_word=int(length_of_word)
            word=s[i:length_of_word+i]
            i=i+length_of_word
            dec.append(word)
        print(dec)
        return dec


            
            

