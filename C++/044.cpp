#include<string>
#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
class Solution {
public:
    bool isMatch(string s, string p);
};
int main()
{
    string input, pattern;
    getline(cin, input);
    getline(cin, pattern);
    Solution *p = new Solution();
    if (p->isMatch(input, pattern)) {
        cout << "True" << endl;
    } else {
        cout << "false" << endl;
    }

}


bool Solution::isMatch(string s, string p)
{
    int i = 0, j = 0;
    bool star = false;
    while (i < s.size() && j < p.size()) {
        while(p[j] == '*') {
            j++;
            star = true;
        }
        if (j == p.size()) {
            return true;
        }
        if (p[j] != '?') {
            if (star) {
                while(i < s.size() && s[i] != p[j])
                    i++;
                if (i == s.size())
                    return false;
                else {
                    i++;
                    j++;
                    star = false;
                }
            } else {
                if (s[i] != p[j]) {
                    return false;
                } else {
                    i++;
                    j++;
                }
            }
        } else {
            j++;
            if(p[j] == '*') {
                continue;
            }
            if (j == p.size()) {
                return true;
            }
            if (star) {
                while(i < s.size() && s[i] != p[j]) {
                    i++;
                }
                if (i == s.size()) {
                    return false;
                } else {
                    i++;
                    j++;
                    star = false;
                }
            } else {
                i++;
                if (s[i] != p[j]) {
                    return false;
                } else {
                    i++;
                    j++;
                }
            }       
        }
    }
    if (i != s.size() || j != p.size()) {
        return false;
    }
    return true;
}
// s = "adceb"
// p = "*a*b"