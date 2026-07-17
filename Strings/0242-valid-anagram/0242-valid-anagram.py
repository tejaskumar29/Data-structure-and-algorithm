class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        charcount={}
        for ch in s:
            charcount[ch]=charcount.get(ch,0)+1
        for ch in t:
            charcount[ch]=charcount.get(ch,0)-1

        for value in charcount.values():
            if value!=0:
                return False
        return True