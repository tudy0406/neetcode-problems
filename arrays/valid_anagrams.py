class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq = [0]*26
        for x in s:
            freq[ord(x) - ord('a')] += 1
        for x in t:
            freq[ord(x) - ord('a')] -= 1
        for count in freq:
            if count != 0:
                return False
        return True
