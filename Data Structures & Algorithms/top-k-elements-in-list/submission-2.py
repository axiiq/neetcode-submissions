class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]

        for n in set(nums):
            i = nums.count(n)
            buckets[i].append(n)

        out = []
        for i in range(len(buckets) - 1, 0, -1):
            if len(out) == k:
                break
            for n in buckets[i]:
                out.append(n)

        return out