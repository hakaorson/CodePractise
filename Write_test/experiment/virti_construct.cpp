#include <iostream>
using namespace std;

class Base
{
    int i;

public:
    int pub_i;
    Base()
    {
        int temp = 0;
        Function();
        cout << "Base constructor" << endl;
    }

    virtual void Function()
    {
        cout << "Base::Fuction" << endl;
    }

    virtual ~Base()
    {
        Function();
        cout << "Base destructor" << endl;
    }
};

class A : public Base
{
public:
    A()
    {
        // Function();
        // cout << "A constructor" << endl;
    }

    virtual void Function()
    {
        cout << "A::Function" << endl;
    }

    virtual ~A()
    {
        Function();
        cout << "A destructor" << endl;
    }
};

int main()
{
    Base *a = new Base;
    delete a;

    cout << "-------------------------" << endl;
    A temp;
    temp.pub_i;
    A *b = new A; //语句1
    delete b;
}