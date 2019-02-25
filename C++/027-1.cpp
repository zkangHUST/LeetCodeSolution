#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
    }
};

int Solution::removeElement(vector<int>& nums, int val)
{
    vector<int>::iterator it;
    int cnt = 0;
    for (it = nums.begin(); it != nums.end(); it++) {
        if (*it != val) {
            cnt++;
        } else {
            
        }   

    }   
}