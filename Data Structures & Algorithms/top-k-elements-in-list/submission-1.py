class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        counts = dict()

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        for num, freq in counts.items():
            buckets[freq].append(num)

        out = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                out.append(n)
                if len(out) == k:
                    return out

