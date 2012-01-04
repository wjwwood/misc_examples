#include <iostream>
#include <boost/bind.hpp>
#include <boost/function.hpp>
#include <yaml.h>

typedef boost::function<void(int)> MyCallback;

void fooCallback(int an_int) {
    std::cout << "From fooCallback free function, an_int: " << an_int << std::endl;
}

// Think of this as the library
class A {
public:
    A() {}
    ~A() {}
    
    void setMyCallback(MyCallback my_callback) {
        this->my_callback = my_callback;
    }
    
    void doCallback(int an_int) {
        this->my_callback(an_int);
    }
private:
    MyCallback my_callback;
};

// Think of this as the driving Application (user)
class B {
public:
    B() {}
    ~B() {}
    
    void barCallback(int an_int) {
        std::cout << "From B.barCallback class method, an_int: " << an_int << std::endl;
    }
    
    void bazCallback(int an_int) {
        std::cout << "From B.bazCallback class method, an_int: " << an_int << std::endl;
    }
    
    void fooCallback(int an_int, int another_int) {
        std::cout << "From B.fooCallback class method, an_int: " << an_int << " and another_int: " << another_int << std::endl;
    }
    
    void doBazCallback() {
        this->a.setMyCallback(boost::bind(&B::bazCallback, this, _1));
        this->a.doCallback(3);
    }
private:
    A a;
};

int main(void) {
    A a;
    B b;
    
    // Using a free (static) function as a callback
    a.setMyCallback(fooCallback);
    a.doCallback(1);
    
    // Using a method function callback with a class reference
    a.setMyCallback(boost::bind(&B::barCallback, &b, _1));
    a.doCallback(2);
    
    // Using a method function callback with a self (this) reference
    b.doBazCallback();
    
    // Adding an additional argument to the callback
    int i = 5;
    a.setMyCallback(boost::bind(&B::fooCallback, &b, _1, i));
    a.doCallback(4);
}