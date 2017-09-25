# Technical Review Notes
Credits for _Cracking the Code Interview, 6th edition_ and _Data Structure and Algorithms in Python_. 

## Time/Space Complexity

### Big-O, Big-Ω, Big-Θ and Little-O
- T(n) is O(f(n)) = growth rate of T(n) <= growth rate of f(n) _Upper Bound_
- T(n) is Ω(f(n)) = growth rate of T(n) >= growth rate of f(n) _Lower Bound_
- T(n) is Θ(f(n)) = growth rate of T(n) == growth rate of f(n)f(n) _Exact Bound_
- T(n) is o(f(n)) = growth rate of T(n)T(n) < growth rate of f(n)f(n) _Upper Bound that does not equal to_


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
  
  
