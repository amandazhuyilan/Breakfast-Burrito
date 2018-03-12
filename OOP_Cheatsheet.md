## Object Oriented Programming Cheatsheet 

### Glossary
- __Abstract Class__ A class whose primary purpose is to define an interface, provide an appropriate base class from which other classes can inherit. An abstract class cannot be instantiated.

A class is made abstract by declaring at least one of its functions as pure virtual function: 

(specified by placing "= 0" in its declaration)

```C++
class Box {
   public:
      // pure virtual function
      virtual double getVolume() = 0;
      
   private:
      double length;      // Length of a box
      double breadth;     // Breadth of a box
      double height;      // Height of a box
};
```

An object-oriented system might be used as an abstract base class to provide a common and standardized interface appropriate for all the external applications, this architecture also allows new applications to be added to a system easily, even after the system has been defined.

- __Class__ A class defines a object's interface and implementation. It specifies the object's internal representation and defines the operation the object can perform.

- __Class Operation__ An operation targeted to a class and not to an individual object. In C++ class operations are called __static member functions__.

- __Constructor Class__ In C++, an operation that is automatically invoked to intialize new instances.
- __Design Pattern__ A design patter systematically names, motivates, and explains a general design that addresses a recurring design problem in object-oriented systems. 
It describes:
  - the problem
  - the solution
  - when to apply the solution
  - the consequences
  - implementation hints and examples
  
  The solution is a general arrangement of object and classes that solve the problem, it is customized and implemented to solve a problem in a particular context.
  
- __Encapsulation__ The result of hiding a representation and implementation in an object. The representation is not visible, cannot be directly accessed from outside the object. Operations are the only way to access and modify an object's representation. In C++ encapsulation and data hiding are supported by __classes__.

- __Inheritance__ Inheritance allows us to define a class in terms of another class, which makes it easier to create and maintain an application. This also provides an opportunity to reuse the code functionality and fast implementation time.
  
  - __Class inheritance__ defines a new class in terms of one or more parent class. The new class inherits its interface and implementation from its parents. The new class is called a __subclass__. Class inheritance includes __interface inheritance__ and __implementation inheritance__. Interface inheritance defines a new interface in terms of one or more exisiting interfaces. Implementation inheritance defines a new implementation in terms of one or more exisiting implementations.
  
A derived class inherits all base class methods with the following exceptions −

  - Constructors, destructors and copy constructors of the base class.
  - Overloaded operators of the base class.
  - The friend functions of the base class.
  
```C++
Example of inheriting from a private/public/protected class
```
- __Instance Variable__ A piece of data that defines part of an object's representation (__Data Member__ in C++).

- __Interface__ An interface describes the behaviour or capabilities for a C++ class without committing to a particular implementation of that class. Interfaces are implemented using abstract classes, abstract classes cannot used to instantiate an object, to be instantiated, it __must__ implement (override) each of the virtual functions.

```C++
class Shape {
   public:
      // pure virtual function providing interface framework.
      virtual int getArea() = 0;
   
   protected:
      int width;
      int height;
};
 
// Derived classes
class Rectangle: public Shape {
   public:
      int getArea() { 
         return (width * height); 
      }
};

class Triangle: public Shape {
   public:
      int getArea() { 
         return (width * height)/2; 
      }
};
 
```

- __Polymorphoism__ Polymorphosm means to have many forms. In C++, polymorphism occurs when there is a hierachy of classes and they are related by inheritance (or have ```virtual``` functions).

C++ polymorphism means that a call to a member function will cause a different function to be executed depending on the type of object that invokes the function.

- __Template__ A template is a blueprint or formula for creating a generic class or function.
  - Function templates:
```C++
template <class type> ret-type func-name(parameter list) {
   // body of function
} 
template <class T>
T GetMax (T a, T b) {
  T result;
  result = (a>b)? a : b;
  return (result);
}

int main () {
  int i=5, j=6, k;
  long l=10, m=5, n;
  k=GetMax<int>(i,j);
  n=GetMax<long>(l,m);
  cout << k << endl; // return 6
  cout << n << endl; //return 10
  return 0;
}

```
  - Class Templates
  
  ```C++
//NEED EXAMPLE HERE
  ```
