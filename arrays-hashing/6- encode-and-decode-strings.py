from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        delimeter = '$'
        for name in strs:
            res += str(len(name)) + delimeter + name 

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0
        while i < len(s):
            j = i 
            while s[j] != '$':
                j += 1
            lenght = int(s[i:j])
            i = j + 1
            j = i + lenght

            res.append(s[i:j])
            i = j
            
        return res


#print(Solution().encode(["neet","code","love","you"])) #4$neet4$code4$love3$you
print(Solution().decode("4$neet4$code4$love3$you"))