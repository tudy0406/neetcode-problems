class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size();
        bool foundRow;
        //search row
        int l = 0, r = m-1;
        int mid;
        while(l<=r){
            mid = (l+r)/2;
            if(target >= matrix[mid][0] && target<=matrix[mid][n-1])
            {
                foundRow = true;
                break;
            }else{
                if(target < matrix[mid][0])
                    r = mid-1;
                else
                    l = mid+1;
            }
        }

        if(!foundRow)
            return false;
        
        //search column
        l = 0; 
        r = n-1;
        int midC;
        while(l<=r){
            midC = (l+r)/2;
            if(matrix[mid][midC] == target)
                return true;
            if(target < matrix[mid][midC])
                r = midC-1;
            else
                l = midC+1;
        }

        return false;
    }
};
