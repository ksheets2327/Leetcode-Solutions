class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()){ return {}; }
        int m = matrix.size();
        int n = matrix[0].size();

        vector<int> ans;

        //boundaries
        int r1 = 0;
        int c1 = 0;
        int r2 = m - 1;
        int c2 = n - 1;

        while (ans.size() < m * n){
            for (int i = c1; i <= c2 && ans.size() < m * n; ++i){
                ans.push_back(matrix[r1][i]);
            }
            r1++;

            for (int j = r1; j <= r2 && ans.size() < m * n; ++j){
                ans.push_back(matrix[j][c2]);
            }
            c2--;

            for (int k = c2; k >= c1 && ans.size() < m * n; --k){
                ans.push_back(matrix[r2][k]);
            }
            r2--;

            for (int l = r2; l >= r1 && ans.size() < m * n; --l){
                ans.push_back(matrix[l][c1]);
            }
            c1++;
        }

        return ans;
        
    }
};
