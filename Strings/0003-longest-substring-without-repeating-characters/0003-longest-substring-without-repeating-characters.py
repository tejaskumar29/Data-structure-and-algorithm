class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index={}
        left=0
        maxlen=0
        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]]>=left:
                left=char_index[s[right]]+1

            char_index[s[right]]=right
            maxlen=max(maxlen,right-left+1)
        return maxlen
        