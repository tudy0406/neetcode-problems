class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charsSeen = set()
        j = 0
        maxLength = 0
        for i, char in enumerate(s):
            while char in charsSeen:
                charsSeen.remove(s[j])
                j+=1
            
            charsSeen.add(s[i])

            maxLength = max(maxLength, i-j+1)
        return maxLength
