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
	void showPosition();
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
	bool	instantSuccess;
};
int main()
{
	string input, pattern;
	//input = "abefcdgiescdfimde";
	//input = "mississippi";
	pattern = "?*?";
	input = "b";
	//pattern = "ab*cd?i*de";
	//pattern = "m??*ss*?i*pi";
	Solution* p = new Solution();
	if (p->isMatch(input, pattern)) {
		cout << "True" << endl;
	}
	else {
		cout << "false" << endl;
	}
	system("pause");

}


bool Solution::isMatch(string s, string p)
{
	init(s, p);

	while (pPos != patternSize) {
		if (instantFail) {
			return false;
		}
		showPosition();
		if (strOver()) {
			return false;
		}
		if (pattern[pPos] == '*') {
			handleStar();
		}
		else if (pattern[pPos] == '?') {
			handleQmark();
		}
		else {
			handNormalChar();
		}
	}

	if (hasStar) {
		return true;
	}
	if (sPos.count(strSize - 1) != 0) {
		return true;
	}
	return false;
}

Solution::Solution()
{
	sPos.insert(-1);
	pPos = 0;
	hasStar = false;
	instantSuccess = false;
}

bool Solution::handleStar()
{
	while (pattern[pPos] == '*') {
		pPos++;
	}
	if (pPos == patternSize) {
		instantSuccess = true;
	}
	hasStar = true;
	return true;
}

bool Solution::handleQmark()
{
	if (hasStar) {
		set<int> tmp;
		for (set<int>::iterator it = sPos.begin(); it != sPos.end(); it++) {
			tmp.insert(*it + 1);
		}
		sPos = tmp;
		pPos++;
	}
	else {
		pPos++;
		set<int> tmp;
		for (set<int>::iterator it = sPos.begin(); it != sPos.end(); it++) {
			tmp.insert(*it + 1);
		}
		sPos = tmp;
	}
	return true;
}
bool Solution::handNormalChar()
{
	int p;

	if (hasStar) {
		set<int> tmp;
		for (set<int>::iterator it = sPos.begin(); it != sPos.end(); it++) {
			p = *it + 1;
			if (p >= strSize) {
				instantFail = true;
				return false;
			}
			while (p < strSize) {
				if (str[p] == pattern[pPos])
					tmp.insert(p);
				p++;
			}
		}
		sPos = tmp;
		hasStar = false;
	}
	else {
		set<int> tmp;
		for (set<int>::iterator it = sPos.begin(); it != sPos.end(); it++) {
			p = *it + 1;
			if (p >= strSize) {
				instantFail = true;
				return false;
			}
			if (str[p] == pattern[pPos]) {
				tmp.insert(p);
			}
		}
		sPos = tmp;
	}
	if (sPos.empty()) {
		instantFail = true;
	}
	pPos++;
	return true;
}
void Solution::showPosition()
{
	cout << "str position: ";
	for (set<int>::iterator it = sPos.begin(); it != sPos.end(); it++) {
		cout << *it << " ";
	}
	cout << endl;
	cout << "pat position: ";
	cout << pPos << endl;
	
}
void Solution::init(const string & s, const string & p)
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
}
