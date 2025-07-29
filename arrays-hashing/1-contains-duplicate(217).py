class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}

        for num in nums:
            if num in nums_dict.keys():
                return True
            else:
                nums_dict[num] = num 
        return False