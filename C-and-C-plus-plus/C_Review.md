### C and C++ Review

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

- For array pointers, the array pointer has to be inititalized with some value:
  ``` int * A[5] ```
  
  ``` delete A ```     This won't work 

``` int * A = new int[5] ```

``` delete A ```      This will work

Arrays and pointers:

Arrays are expensive: when created an array with 5 elements: 

```Person * pArray[5]```

This will call the ```Person``` Constructor 5 times to create each Person object.

However, if we use pointers, ```Person *p``` the space will only be allocated when the pointers are called and used. 



