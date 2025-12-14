class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        freq = [0] * 26
        
        for string in strs:
            for i in range(26):
                freq[i] = 0
            for ch in string:
                freq[ord(ch)-ord('a')] += 1
            
            key = tuple(freq)
            if key not in results:
                results[key] = []
            
            results[key].append(string)
        
        return list(results.values())