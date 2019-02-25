#include<iostream>
#include<cstring>
using namespace std;
class Queen {
private:
    int *p;
    int cnt;
    bool check(int m);
public:
    Queen(int n); 
    void backtrace(int m, int n);
    int getTotalNum();
    ~Queen();
};
Queen::Queen(int n)
{
    cnt = 0;
    p = new int[n];
    memset(p, 0, n * sizeof(int));
}
bool Queen::check(int m)
{
    for(int i = 0; i < m; i++) {
        if (p[i] == p[m] || abs(p[i] - p[m]) == m - i) {
            return false;
        }
    }
    return true;
}
void Queen::backtrace(int m, int n)
{
    if (m == n) {
        cout << '[';
        for (int i = 0; i < n; i++) {
            cout << p[i] << " ";
        }
        cout << ']';
        cnt++;
        cout << endl;
        return;
    }
    for (int i = 0; i < n; i++) {
        p[m] = i;
        if (check(m) == true) {
            backtrace(m + 1, n);
        }
    }
    return;
}
int Queen::getTotalNum()
{
    return cnt;
}
Queen::~Queen()
{
    delete p;
}
int main()
{
    Queen a(8);
    a.backtrace(0, 8);
    cout << a.getTotalNum() << endl;
    return 0;    
}