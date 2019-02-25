class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int rom,col;
        rom=nums.size();
        col=nums[0].size();
        vector<vector<int>>  ans;
        vector<int> temp;
        if(rom*col!=r*c)
            return nums;
        int i,j;
        int count = 0;
        int m=0,n=0;
        for(i=0;i<rom;i++)
            for(j=0;j<col;j++)
            {
                count++;
                temp.push_back(nums[i][j]);//临时变量存储矩阵每一行的值
                if(count==c)
                {
                    ans.push_back(temp);
                    count=0;
                    temp.clear();
                }
            }
            return ans;
    }
};
