# Technical Review Notes 2017
Credits for _Cracking the Code Interview, 6th edition_ and _Data Structure and Algorithms in Python_. 

## Strings and Arrays

### ASCII and UNICODE 
ASCII defines 128 characters,mapping to 0-127 characters. Unicode defines 2<sup>21</sup> characters.
Unicode is a superset of ASCII, and the numbers 0–128 have the same meaning in ASCII as they have in Unicode.

Because Unicode characters don't generally fit into one 8-bit byte, there are numerous ways of storing Unicode characters in byte sequences, such as UTF-32 and UTF-8.

### C++ Review
#### Vector 
* Can change size dynamically.
* Operations: front, back, push_back, pop_back
* vector<int> is non-array, non-reference, and non-pointer - it is being passed by value, and hence it will call copy-    constructor. Must use vector<int>& to pass it as reference.
  
  
