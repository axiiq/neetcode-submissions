class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = c_index = 0
        for i, v in enumerate(nums):
            c = target - v
            start = i

            if c in nums[i+1::]:
                return [start, nums[i+1::].index(c)+start+1]
                