class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        l, r = 0, n-1
        max_area = 0

        while l < r:
            width = r - l
            height = min(heights[l],heights[r])

            new_area = width * height

            if new_area > max_area:
                max_area = new_area

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area