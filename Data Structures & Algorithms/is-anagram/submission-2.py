class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        for ch in s:
            hm[ch] = hm.get(ch,0) + 1
        for ch in t:
            hm[ch] = hm.get(ch,0) - 1

        for value in hm.values():
            if value!=0:
                return False
        return True