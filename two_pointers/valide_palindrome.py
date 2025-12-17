class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set()
        maxLength = 0
        currLength = 0
        for num in nums:
            sequence.add(num)
        
        for num in nums:
            if num-1 in sequence:
                continue
            else:
                cnum = num+1
                currLength = 1
                while cnum in sequence:
                    currLength+=1
                    cnum+=1
                if currLength > maxLength:
                    maxLength = currLength
        return maxLength
