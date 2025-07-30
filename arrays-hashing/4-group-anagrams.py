from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        map = {} # ordered_word -> list of anagrams
        print(map)
        for word in strs:
            ordered_word = ''.join(sorted(word))

            if ordered_word in map:
                map[ordered_word].append(word) 
            else:
                map[ordered_word] = [word]

        
        for i in map.values():
            result.append(i)

        return result 
    

#strs = ["act","pots","tops","cat","stop","hat"]

result = Solution().groupAnagrams(["act","pots","tops","cat","stop","hat"])
print(result)