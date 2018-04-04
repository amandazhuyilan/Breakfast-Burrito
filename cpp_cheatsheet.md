## CS3520 C++ Notes

__Always check for NULL for function inputs and previous initiailzed pointers___

##### ```int main(int argc, char * argv[], char * envp[])```

```int argc``` counts the number of command line arguments that ```argv[]``` holds for this current program execution, includes the object program itself, hence must be >= 1, is ```main()```’s first formal parameter.

```char * argv[]``` is a pointer to the list of actual const string arguments.2nd formal parameter of ```main()```; optional; if specified, the first parameter ```argc``` must already be specified.

```char * envp[]``` holds environment variables as string constants, plus the header: ```PATH=```. 3rd formal and optional parameter of ```main()```.

#### Pointers

```&``` is the address of operator, and can be read simply as "the address of".

```*``` is the dereference operator, and can be read as "value pointed to by".

[Tutorials from cplusplus.com](http://www.cplusplus.com/doc/tutorial/pointers/) about pointers.

```int * p``` -> initalizing a memory space at 0X0112 and setting it as NULL

```p = new int(12) ``` -> initalizing a new memory space at memory location 0X2222 and setting it as 12

```cout << p ``` -> will print 0x2222

```cout << &p ``` -> will print 0x0112

```cout << *p ``` -> will print 12

When deleting a pointer:

```delete p``` -> will delete 12 in 0x2222

``` p = NULL``` -> not necessary, will set 0x0112 to NULL
``` delete [] c ``` -> only need [] when the char * is initialized with []
### [Smart Pointers](https://github.ccs.neu.edu/amandazhuyilan/CCIS3520-C-plus-plus/blob/master/smartPointers.cpp)

[smart pointers in ```Boost```](https://stackoverflow.com/questions/569775/smart-pointers-boost-explained)

__Difference between call by reference and call by pointer?__
- References are never ```null```, but pointers may be ```null``` or pointing to invalid memory.
- Pointers can be reassigned while references can only be assigned at initialziation.
- Pointers are iterable in arrays, therefore References are usually preferred over pointers whenever we don’t need “reseating”.
- Use references when you can, and pointers when you have to.

### Inheritence 

Functions and variables are set as ```private``` by default.

```virtual void hello() = 0;``` -> Whenever another class inherits from this class, the ```hello``` function is forced to be inherited.

```A * a = new B()``` This will can only call functions in A unless it's virtual. For virtual funtions, B version will be called. Have to set both A and B functions virtual.

If there is a ```virtual``` function, we need to add a virtual delete in the child class. Also because ```virtual``` is for pointer and references.

#### Vectors

__How does vectors know when to increment vector size?__

Whenever the vector hits max, it will automatically double the size.
```
for (auto iter = myVector.begin(); itr != myVector.end(); iter++)
  cout << *iter << endl;
```

Adding an object in a vector without having to copy the object:

```vector.emplace(vector.start(), "name", value)```

#### lamnda functions
```cpp 
auto myFunction = [](int & val){val *= 2};
int val10 = 10;
myFunction(val10);
cout << val10 << endl;        // will print 20
```
 
#### Templates

Write the template in the hpp file, not in the cpp file, or else it won't be linked to the cpp file.

```c++
template <typename T, typename U> void add (T a, U b){
    cout << a + b << endl;
}
```
In main function:

```c++
add<int>(5,5);
add<int, double>(5, 5.5)
add<int, string>(5, "hello") // error
```

If want to make a unique pointer, we can put the copy constructor into the private section.

### Stacks

```c++
stack<char> mystack;
input = "(This is an example!)";
 
bool balanced false;
for (int i = 0; i < input.size(); i++){
    char c input[i];
    if (c =='('){
        mystack.push(c);
    }else if (c ==')'){
        if (mystack.empty()){
            balanced = false;
            break;
        }
        mystack.pop();
    }
    
    return 0;
}
```

### Debugging Segmentation Faults
- Compile your application with ```-g```, then you'll have debug symbols in the binary file.
- Use ```gdb``` to open the gdb console.
- Use ```file``` and pass it your application's binary file in the console.
- Use ```run``` and pass in any arguments your application needs to start.
- Type ```bt``` in the gdb console to get a stack trace of the Segmentation Fault.
