class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split()
        for w in words:
            return len(words[-1])