## Python Cheatsheet

```python 
#!/usr/bin/env python

def main():
    """ Main program """
    # Code goes over here.
    return 0

if __name__ == "__main__":
    main()
```

```__name__``` is a built-in variable which evaluates to the name of the current module. However, if a module is being run directly (as in myscript.py above), then ```__name__``` instead is set to the string ```"__main__"```. This will be useful to test whether your script is being run directly or being imported by something else.

### Handling Exceptions
This [guide](http://hplgit.github.io/primer.html/doc/pub/input/._input-readable007.html) is exceptionally helpful.

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

### ```sys.argv``` 
```sys.argv``` is a list in Python, which contains the command-line arguments passed to the script.

```python
import sys

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))
```

### Trees
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
```

