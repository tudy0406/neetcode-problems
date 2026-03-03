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
    void kthSmallestAux(TreeNode* root, int* k, int *result){
        if(!root)
            return;
        kthSmallestAux(root->left, k, result);
        if(*k == 1)
            *result = root->val;
        --*k;
        kthSmallestAux(root->right, k, result);
    }

public:
    int kthSmallest(TreeNode* root, int k) {
        int result = 0;
        kthSmallestAux(root, &k, &result);
        return result;
    }
};
