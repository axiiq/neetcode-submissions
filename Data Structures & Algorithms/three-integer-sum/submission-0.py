class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            # if the lowest number is greater than zero, it's not possible to make the sum == 0
            if nums[i] > 0:
                break
            
            # skip the recurring numbers
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            lo, hi = i+1, n-1

            while lo < hi:
                
                summ = nums[i] + nums[lo] + nums[hi]

                if summ == 0:
                    ans.append([nums[i],nums[lo],nums[hi]])
                    lo, hi = lo+1, hi-1

                    # skip the recurring numbers
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    
                    # skip the recurring numbers
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1

                # sum too small, shift low index up
                elif summ < 0:
                    lo += 1

                # sum too big, shift high index down
                else:
                    hi -= 1

        return ans