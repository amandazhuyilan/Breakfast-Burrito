## Python Cheatsheet

### List:
- Sort a list: ``` nums.sort()```
- Get the last element of list: ```list[-1]```
- Reverse a list: ```list[::-1]```
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

- ```string.isalpha``` and ```string.isdigit``` for alphabet and digit determination.

### Numbers
To get the largest/smallest int:
```
import sys
max_num = sys.maxint
min_num = -sys.maxint
```

