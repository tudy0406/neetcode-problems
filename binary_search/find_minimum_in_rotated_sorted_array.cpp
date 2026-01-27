class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0, r = nums.size()-1;
        int mid;
        int res = INT_MAX;
        while(l<=r){
            mid = (l+r)/2;
            res = min(res, nums[mid]);
            if(nums[mid] >= nums[r])
                l = mid+1;
            else
                r = mid-1;
        }
        return res;
    }
};
