class Solution:
    def isPalindrome(self, s: str) -> bool:
        helper = ""
        s = s.lower().replace(" ","")
        
        for c in s:
            if c.isalnum():
                helper += c
                
        return helper == helper[::-1]