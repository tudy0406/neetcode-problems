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

public:
    vector<int> rightSideView(TreeNode* root) {
        queue<TreeNode*> q;
        vector<int> results;
        TreeNode *aux = nullptr;
        if(root)
            q.push(root);
        while(!q.empty()){
            int levelSize = q.size();
            for(int i = 0; i<levelSize; i++){
                aux = q.front();
                q.pop();

                if(i == levelSize - 1)
                    results.push_back(aux->val);

                if(aux->left)
                    q.push(aux->left);
                if(aux->right)
                    q.push(aux->right);
            }
        }
        return results;
    }
};
