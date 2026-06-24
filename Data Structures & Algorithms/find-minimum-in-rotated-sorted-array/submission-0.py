class Solution:
    def findMin(self, nums: List[int]) -> int:
        best_min = float('inf')

        for num in nums:
            if num < best_min:
                best_min = num
            
        return best_min