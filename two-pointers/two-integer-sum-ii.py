from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize two pointers and iterate.
        # curSum >= target and lp + rp != target? rp moves left
        # else lp moves right
        # return indexes with +1 (response must be 1-indexed)
        lp, rp = 0, len(numbers) - 1

        while lp < rp:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

#numbers = [1,2,3,4], target = 3, result [1, 2]
#numbers = [1,2,3,4], target = 6, result [2, 4]


print(Solution().twoSum([1,2,3,4], 6))