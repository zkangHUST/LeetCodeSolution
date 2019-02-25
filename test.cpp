#include<iostream>
#include<cstring>
using namespace std;
class A {
    public:
        void print() {
            cout<<"A::print()"<<endl;
        }
};
class B:public A {
    public:
        B() {

        }
        virtual void print() {
        
        }
};

int main()
{
    A a;
    cout << sizeof(A);
    return 0;
}