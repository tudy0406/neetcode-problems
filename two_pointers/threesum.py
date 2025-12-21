class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    if (nums[i], nums[j], nums[k]) not in result:
                        result.append((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1    
                    continue
                if nums[j]+nums[k] < -nums[i]:
                    j+=1
                    continue
                if nums[j]+nums[k] > -nums[i]:
                    k-=1
                    continue
        return result            
        