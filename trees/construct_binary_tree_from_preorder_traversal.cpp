/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
    private:
    int preorderIndex = 0;
    unordered_map<int, int> inorderMap;

    TreeNode* buildHalfTree(vector<int>& preorder, vector<int>& inorder, int left, int right){
        
        if(left>right){
            return nullptr;
        }
            
        TreeNode* node = new TreeNode(preorder[preorderIndex]);
        
        ++preorderIndex;

        int j = inorderMap[node->val];
        node->left = buildHalfTree(preorder, inorder, left, j-1);    
        node->right = buildHalfTree(preorder, inorder, j+1, right);
        
        return node;
    }

public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for(int i = 0; i < inorder.size(); i++)
            inorderMap[inorder[i]] = i;
        TreeNode* absoluteRoot = buildHalfTree(preorder, inorder, 0, inorder.size()-1);
        return absoluteRoot;
    }
};
