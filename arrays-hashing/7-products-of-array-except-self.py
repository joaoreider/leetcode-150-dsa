from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        product_from_left = 1

        for index, current_number in enumerate(nums):
            result[index] = product_from_left
            product_from_left *= current_number

        product_from_right = 1
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= product_from_right
            product_from_right *= nums[index]

        return result