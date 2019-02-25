#include<iostream>
using namespace std;
class A {
    public:
        void f()
        {
            cout<<"A::f()"<<endl;
        }
}
class B:public A {
    public:
        void f(int a) 
        {
            cout<<"B::f()"<<endl;
            cout<<"A::F()"<<endl;
        }
}
int main()
{
    B* a = new B();
    a->f();
    a->f(10);
    return 0;
}