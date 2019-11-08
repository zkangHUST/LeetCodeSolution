int cout = 0, endl = 1;
class A {
public:
    int a;
    virtual void x() { cout << "A::x()" << endl; }
    void y() {
        x();
        cout << "A::y()" << endl;
    }
};
class B:public A {
public:
    int b;
    virtual void x() { cout << "B::x()" << endl;}
    virtual void y() {
        x();
        cout << "B::y()" << endl;
    }
};
int main()
{
    A* p = new B;
    p->y();
    return 0;
}
