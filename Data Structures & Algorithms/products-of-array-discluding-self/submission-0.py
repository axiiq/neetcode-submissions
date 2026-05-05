class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if j != i:
                    prod *= nums[j]
            out[i] = prod

        return out
