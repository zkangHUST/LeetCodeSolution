#include<iostream>
using namespace std;
class A {
public:
    virtual void x() {
        cout << "A::x()" << endl;
    }
    void y() {
        x();
        cout << "A::y()" << endl;
    }
};
class B:public A {
public:
    virtual void x() {
        cout << "B::x()" << endl;
    }
    virtual void y() {
        x();
        cout << "B::y()" << endl;
    }
};
int main()
{
    A* p = new B;
    p->y();
    // cout << "----" << endl;
    // q->y();
    return 0;
}
