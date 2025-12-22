class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, maxF = 0, 0, 0
        result = 0
        charsFreq = {}
        for r in range(len(s)):
            charsFreq[s[r]] = 1 + charsFreq.get(s[r], 0)
            maxF = max(maxF, charsFreq[s[r]])

            while (r-l+1) - maxF > k:
                charsFreq[s[l]]-=1
                l+=1

            result = max(result, (r-l+1))
                
        return result
                

            
