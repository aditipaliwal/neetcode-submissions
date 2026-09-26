class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s = clean_s+char.lower()
        # print( clean_s,clean_s[::-1])
        if clean_s == clean_s[::-1]:
            return True
        return False