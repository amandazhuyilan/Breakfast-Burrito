## Python Cheatsheet

### Python 103 - Memory Model and Best Practises
#### Objects and References
- Objects are allocated on assignment.
- All objects are passed by __reference__.
    - References area also called _aliases_.
    - Every object has an extra field called reference count that is increased or decreased when a pointer to an object is copied or deleted.
        `refcount` increment examples:
        - Object is created and assigned. (`foo = 'abc'`)
        - Additional alises for it is created. (`bar = foo`)
        - Object passed to a function (new local reference) `(spam(foo)`)
        - Object becomes part of a container object. (`manyFoo = [foo, 'xyz']`)
    - Objects are garbage-collected when the reference count goes to 0.
    - Global variable's reference count never goes to 0.
    - Check the number of current references using `sys.getrefcount` function.

#### `is` and `==`
- `is` is an object identity (pointer) comparisor, `==` is an object value comparisor.
- Use `is` when comparing singletons (`True`, `False`, `None`).


#### Copying Objects
- Trickier with mutable objects: list, dictionary, set and user-defined classes.
- copying `a` to `b`:
    - Creating an alias is not a copy: `a = b`
        - `a == b` and `a is b` (`id(a) == id(b)`)
    - Creating a shallow copy (all objects 'copied' as aliases):
        - `b = a[:]` # `a == b` but `a is not b`
    - Creating a deep copy (all objects 'copied' are copies)
        - `b = copy.deepcopy(a)`
        

#### `__main__`

```python 
#!/usr/bin/env python

def main():
    """ Main program """
    # Code goes over here.
    return 0

if __name__ == "__main__":
    main()
```

```__name__``` is a built-in variable which evaluates to the name of the current module. However, if a module is being run directly (as in myscript.py above), then ```__name__``` instead is set to the string ```"__main__"```. 

The file can be usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file. This will be useful to test whether your script is being run directly or being imported by something else.

### Handling Exceptions and Errors
This [guide](http://hplgit.github.io/primer.html/doc/pub/input/._input-readable007.html) is an exceptionally good example.

### List:
- Sort a list: ``` nums.sort()```
- Get the last element of list: ```list[-1]```
- Reverse a list: ```list[::-1]```
- Iterate the list in reverse order: ``` for i in range(len(list)-1, 0, -1)```
- Remove the __first__ element of the list with value ```x```: ```list.remove(x)```
- Remove the __last__ element of the list: ```list.pop()```
- Append a new sublist into a list: ```mainset.append([] + subset)```
- Create a row x col matrix: ```matrix = [[0 for x in range(col)] for y in range(row)]```

### String:
- ```string.find()```: If substring exists inside the string, it returns the lowest index where substring is found.
If substring doesn't exist inside the string, it returns -1.
- ```string.join()```: Joins a string seperated by the ```string```element. 
  - convert list to string: ```''.join(list)```
  
```
s = "-"
seq = ("a", "b", "c"); 
print(s.join( seq ))
```
Will print ```a-b-c```.

```string.split(",")```: splits the substrings in the string by the given character and return a list of the substrings.
```python
s = "a,b,c"
print(s.split(s))   # will print ["a","b","c"]
```

- ```string.isalpha``` and ```string.isdigit``` for alphabet and digit determination.

### Numbers
To get the largest/smallest int:
```
import sys
max_num = sys.maxint
min_num = -sys.maxint
```

### ```lambda``` functions

Lamda operators are small annoymous functions with a general syntax of: ```lambda argument_list: expression```
```python
f = lambda x,y: x+y
f(1,1) # will print 1+1 = 2
```
```python
sorted(['Some', 'words', 'sort', 'differently'], key=lambda word: word.lower())
```

Will print ```['differently', 'Some', 'sort', 'words']```.

### ```Map``` functions
Map is a function with two arguments: ``` r = map(func, seq)``` where ```func``` is the name of a function and ```seq``` is a sequence applied to the function ```func```.
```python
def farenheit(T):
    return ((float(9)/5) * T + 32)
def celsius(T):
    return(float(5)/9 * (T - 32))
temp = [10, 20, 30]
F = map(farenheit, temp)
C = map(celsius, temp)
```

If using ```lambda``` operators:
```python
temp = [10, 20, 30]
Farenheit = map(lambda x: ((float(9)/5) * T + 32))
Celsius = map(lambda x: (float(5)/9 * (T - 32))
```

### Filter functions
```filter(func, list)``` provides a way to filter out the elements of the list, for which the ```func``` returns true.
```python 
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)  # [0, 2, 8, 34]
```
### Modifing contents of json files and generate new ones with `jsonpointer`
```
from jsonpointer import set_pointer
from jsonpointer import resolve_pointer

for i in range(100):
    set_pointer(yaml_dict, '/agents/0/actions/0/follow_lane/speed', 10 + i/10)
    set_pointer(yaml_dict, '/agents/1/actions/0/follow_lane/speed', 12 + i/10)

    with open('agents_follow_maliput_{}.yml'.format(i), 'w+') as yaml_file:
        yaml.dump(yaml_dict, yaml_file, default_flow_style=False)
```

### ```sys.argv``` 
```sys.argv``` is a list in Python, which contains the command-line arguments passed to the script.

```python
import sys

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))
```

### Dynamically Printing Multiple Lines on Console
```
# cursor up one line
sys.stdout.write('\x1b[1A')
# delete last line
sys.stdout.write('\x1b[2K')
```

### `Unittest`ing

- Dealing with Error and Exceptions
```
with self.assertRaises(TypeError) as cm:
    failure.fail()
self.assertEqual(
    'The registeraddress must be an integer. Given: 1.0',
    str(cm.exception)
)
```
