class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> preffix(height.size());
        vector<int> suffix(height.size());

        preffix[0] = height[0];
        for(int i = 1; i<height.size(); ++i)
            preffix[i] = max(preffix[i-1], height[i]);

        suffix[height.size()-1] = height[height.size()-1];
        for(int i = height.size()-2; i>=0; --i)
            suffix[i] = max(suffix[i+1], height[i]);

        int totalWater = 0;
        for(int i = 0; i<height.size(); ++i)
            totalWater += min(preffix[i], suffix[i]) - height[i];


        return totalWater;
    }
};
