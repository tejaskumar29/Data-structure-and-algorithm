class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
    
    # Traverse both strings
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Character matched, move pointer for s
            j += 1      # Always advance pointer for t
        
    # If i reached the end of s, all characters were found in order
        return i == len(s)