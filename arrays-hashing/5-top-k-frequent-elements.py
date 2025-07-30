from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        
        sorted_items = sorted(map.items(), reverse=True, key= lambda x: x[1])
        return [x[0] for x in sorted_items[:k]]





result1 = Solution().topKFrequent([1,2,2,3,3,3], 2) # [2, 3]
print(result1)
result2 = Solution().topKFrequent([7,7], 1) # [7]
print(result2)