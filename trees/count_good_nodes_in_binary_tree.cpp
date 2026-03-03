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
    int goodNodes(TreeNode* root) {
        stack<pair<TreeNode*, int>> s;
        int nrNodes = 0;
        if(!root)
            return 0;

        nrNodes = 1;
        s.push({root, root->val});
        TreeNode* aux;
        int auxVal;
        while(!s.empty()){
            aux = s.top().first;
            auxVal = s.top().second;
            s.pop();
            if(aux->left){
                if(aux->left->val >= auxVal)
                    ++nrNodes;
                s.push({aux->left, max(auxVal, aux->left->val)});
            }
            if(aux->right){
                if(aux->right->val >= auxVal)
                    ++nrNodes;
                s.push({aux->right, max(auxVal, aux->right->val)});
            }
        }
        return nrNodes;
    }
};
