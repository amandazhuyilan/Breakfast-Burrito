Catro Street consists of technical review notes of knowledge for data structures, algorithms and essential computer knowledge. Solved questions completed in Python 3 from the [Green Bible](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850/ref=sr_1_1?ie=UTF8&qid=1505751073&sr=8-1&keywords=crack+the+coding+interview) and [Leetcode](http://www.leetcode.com) would be available. This readme consists of a list of links to the contents of the repo.

## Table of Contents 
[Technical Review Notes](https://github.com/amandazhuyilan/Castro-Street/edit/master/Tech_Review_2017.md)

[Data Structure implementations](#Data_Structure)

[Sorting Algorithms](#Sorting_Algorithms)

[Cheat Sheets](#Cheat_Sheets)  

[Problems and Solutions](#Problems_and_Solutions)

<a name="Data_Structure"></a>
### Data structure implementations
* [Binary Search Trees](https://github.com/amandazhuyilan/Castro-Street/blob/master/Data-Structures/BinarySearchTree.py)

* [Red Black Trees](https://github.com/amandazhuyilan/Castro-Street/blob/master/Data-Structures/LinkedList.py)

* [Linked lists](https://github.com/amandazhuyilan/Castro-Street/blob/master/Data-Structures/LinkedList.py)
  - Loop detecting: 

<a name="Sorting_Algorithms"></a>
### Sorting Algorithms
* [Counting Sort](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/CountingSort.py)
  
  Sorting on O(n). Uses an auxiliary array that holds the number of elememts that equal to the index of Index_Arr. 
  Based on the number of entires specified in the Index_Arr, the Out_Arr stores the sorted array in an ascending order.
  
* [Heap Sort](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/HeapSort.py)

* [Quick Sort](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/QuickSort.py)

* [Insertion Sort](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/InsertionSort.py)

  An efficient algorithm for sorting a small number of elements. Time complexity: Best O(n), Worst: O(n<sup>2</sup>).

* [Merge Sort](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/MergeSort.py)

  A divide, conquer and combine recursive sorting algorithm. Time complexity: O(n log(n)).
  
### Searching Algorithms 
* [Breadth First Search](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/BFS.py)

* [Depth First Search](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/DFS.py)
  

<a name="Problems_and_Solutions"></a>
## Problems and Solutions
1. [Two sums](https://github.com/amandazhuyilan/Castro-Street/blob/master/twoSums.py)

  Returns the indices of two numbers in the input array that add up to the target number.

  * Solution 1: Brute force, O(n<sup>2</sup>) 
  * Solution 2: Dictionary. O(n). Set buffer_dictionary[target-nums[i]] = i if nums[i] not in buffer dictionary.  
  
  `TEST_CASE = ([1,4,5,10,3], 7)`
  
  Output: `[1,4]`
  
2. [Is Unique](https://github.com/amandazhuyilan/Castro-Street/blob/master/isUnique.py)
  Checks if the characters in the input string is unique. O(n).
  
3. [URLify](https://github.com/amandazhuyilan/Castro-Street/blob/master/URLify.py)
  Replaces the space(s) of input string.
  
4. [set Zeroes Matrix](https://github.com/amandazhuyilan/Castro-Street/blob/master/Problems-and-Solutions/setZeroMatrix.py)
  Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
  
<a name= "Cheat_Sheets"></a>
### Cheat Sheets
  - [Big Oh](http://bigocheatsheet.com/)
  - [Time Complexity Cheat Sheet](https://www.packtpub.com/sites/default/files/downloads/4874OS_Appendix_Big_O_Cheat_Sheet.pdf)
  - [HTML](http://www.simplehtmlguide.com/cheatsheet.php)
