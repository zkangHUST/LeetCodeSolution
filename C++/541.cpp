#include<algorithm>
class Solution {
public:
    string reverseStr(string s, int k) {
    string::iterator it = s.begin();
    int cnt = s.length()/(2*k);
    int left = s.length()%(2*k);
    while(cnt)
    {
        reverse(it,it+k);
        it+=2*k;
        cnt--;
    }
    if(left<k)
        reverse(it,s.end());
    else if(left<2*k)
        reverse(it,it+k);
    return s;
    }
};
