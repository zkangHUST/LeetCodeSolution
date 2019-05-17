#include<string>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<vector>
#include<set>
using namespace std;
class Solution {
public:
    bool isMatch(string s, string p);
    bool handleStar();
    bool handleQmark();
    bool handNormalChar();
    Solution();
private:
    void init(const string& p, const string& s);
    bool strOver();
private:
    set<int> sPos; 
    int     pPos;   
    bool    hasStar;
    string  str;
    string  pattern;
    int     strSize;
    int     patternSize;
    bool    instantFail;
};
int main()
{
    string input, pattern;
    // getline(cin, input);
    // getline(cin, pattern);
    input = "abefcdgiescdfimde";
    pattern = "ab*cd?i*de";
    Solution *p = new Solution();
    if (p->isMatch(input, pattern)) {
        cout << "True" << endl;
    } else {
        cout << "false" << endl;
    }

}


bool Solution::isMatch(string s, string p)
{
    init(s, p);

    while(pPos != patternSize) {
        if(strOver()) {
            return false;
        }
        if (pattern[pPos] == '*') {
            handleStar();
        } else if (pattern[pPos] == '?') {
            handleQmark();
        } else {
            handNormalChar();
        }
    }
}

Solution::Solution()
{
    sPos.insert(0);
    pPos = 0;
    hasStar = false;
}

bool Solution::handleStar()
{
    while(pattern[pPos] == '*') {
        pPos++;
    }
    hasStar = true;
}

bool Solution::handleQmark()
{
    if (hasStar) {
        pPos++;
    } else {
        set<int> tmp;
        for (set<int>::iterator it = sPos.begin(); it != sPos.end(); it++) {
            tmp.insert(*it + 1);
        }
    }
}
bool Solution::handNormalChar()
{
    int p;

    if (hasStar) {
        set<int> tmp;
        for (set<int>::iterator it = sPos.begin(); it != sPos.end(); it++) {
            p = *it;
            while(p < strSize) {
                if (str[p] == pattern[pPos])
                    tmp.insert(p);
                p++;
            }
        }
        sPos = tmp;
        hasStar = false;
    } else {
        set<int> tmp;
        for (set<int>::iterator it = sPos.begin(); it != sPos.end(); it++) {
            p = *it + 1;
            if (str[p] == pattern[pPos]) {
                tmp.insert(p);
            }
        }
        sPos = tmp;
    }
    if (sPos.empty()) {
        instantFail = true;
    }
}
void Solution::init(const string& p, const string& s)
{
    str = s;
    pattern = p;
    strSize = s.size();
    patternSize = pattern.size();
    instantFail = false;
}

bool Solution::strOver()
{
    for (set<int>::iterator it = sPos.begin(); it != sPos.end(); it++) {
        if (*it != strSize) {
            return false;
        }
    }
    return true;
}// s = "adceb"
// p = "*a*b"