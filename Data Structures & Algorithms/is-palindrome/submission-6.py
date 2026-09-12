class Solution:
    def isPalindrome(self, s: str) -> bool:
        f=""
        for i in s:
            if i.isalnum():
                f+=i
        f=f.lower()
        return f==f[::-1]