## Python Cheatsheet

### List:
- Sort a list: ``` nums.sort()```
- Get the last element of list: ```list[-1]```
- Reverse a list: ```list[::-1]```
- Remove the last element of the list: ```list.pop```
- Append a new sublist into a list: ```mainset.append([] + subset)```
- Create a row x col matrix: ```matrix = [[0 for x in range(col)] for y in range(row)]```

### String:
- ```string.find()```: If substring exists inside the string, it returns the lowest index where substring is found.
If substring doesn't exist inside the string, it returns -1.
- ```string.join()```: Joins a string seperated by the ```string```element.
```
s = "-"
seq = ("a", "b", "c"); # This is sequence of strings.
s.join( seq )
```
Will print ```a-b-c```

- ```string.isalpha``` and ```string.isdigit``` for alphabet and digit determination.
