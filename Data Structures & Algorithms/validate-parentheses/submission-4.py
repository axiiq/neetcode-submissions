class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}":"{", ")":"(", "]":"["}
        stack = []

        for char in s:
            # if char is an open bracket
            if char not in hashmap:
                stack.append(char)
            else:
                # checking if stack is empty
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hashmap[char]:
                        return False
        
        return not stack

