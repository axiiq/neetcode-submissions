class Solution:
    def isPalindrome(self, s: str) -> bool:
        helper = ""
        s = s.lower().replace(" ","")
        
        for c in s:
            if c.isalnum():
                helper += c

        if helper[::1] != helper[::-1]:
                return False
        return True