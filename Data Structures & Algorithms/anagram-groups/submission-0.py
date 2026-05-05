class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()

        for s in strs:
            count = []
            for i in range(26):
                count.append(0)

            for c in set(s):
                index = ord(c) - ord('a')
                count[index] = s.count(c)

            key = tuple(count)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)

        return [i for i in hashmap.values()]



