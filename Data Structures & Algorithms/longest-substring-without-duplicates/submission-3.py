class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        sett = set()
        n = len(s)

        for r in range(n):
            # while substring is invalid
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            w = (r - l) + 1
            max_len = max(max_len, w)
            sett.add(s[r])

        return max_len