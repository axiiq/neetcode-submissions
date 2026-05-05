class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        starters = set()
        s_nums = set(nums)
        for n in s_nums:
            if n-1 not in s_nums:
                starters.add(n)

        for s in starters:
            i = 0
            while True:
                if s+i in s_nums:
                    i+=1
                else:
                    break
            if counter < i:
                counter = i

        return counter   
                
            


