class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        kFreqValues = []
        maxFreq = 0
        i = 0
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1
            if freqMap[num] > maxFreq:
                maxFreq = freqMap[num]
        
        buckets = [[] for _ in range(len(nums)+1)]
        
        for key, value in freqMap.items():
            buckets[value].append(key)

        for freq in range(maxFreq, 0, -1):
            for num in buckets[freq]:
                kFreqValues.append(num)
                k -= 1
                if k == 0:
                    return kFreqValues
        return kFreqValues
