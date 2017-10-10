Castro Street consists of technical review notes of knowledge for data structures, algorithms and essential computer knowledge. Solved questions completed in Python 3 from [Cracking the Code Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850/ref=sr_1_1?ie=UTF8&qid=1505751073&sr=8-1&keywords=crack+the+coding+interview) and [Leetcode](http://www.leetcode.com) would be available. This readme consists of a list of links to the contents of the repo.

## Table of Contents 
[Technical Review Notes](https://github.com/amandazhuyilan/Castro-Street/edit/master/Tech_Review_2017.md)

[Data Structure implementations](#Data_Structure)

[Sorting Algorithms](#Sorting_Algorithms)

[Cheat Sheets](#Cheat_Sheets)  

[Problems and Solutions](#Problems_and_Solutions)

<a name="Data_Structure"></a>
### Data structures
* [Binary Search Trees](https://github.com/amandazhuyilan/Castro-Street/blob/master/Data-Structures/BinarySearchTree.py)

  - A binary search tree is a binary tree in which all left decendents <= n <= all right decendents.
  
  - Complete binary tree: every level is filled except for perhaps the last level.
  - Full binary tree: every node has zero or two children.
  - Perfect binary tree: both full and complete.
  
  Binary Tree Traversals
  - In-order: 
    ```
    while node != None
      
        InOrderTraversal(node.left)
        
        visit(node)
        
        InOrderTraversal(node.right)
    ```
     
  - Pre-order: 
    ```
    while node != None
      
        visit(node)
        
        PreOrderTraversal(node.left)
        
        PreOrderTraversal(node.right)
    ```
      
  - Post-order: 
    ```
      while node != None
      
        PostOrderTraversal(node.left)
        
        PostOrderTraversal(node.right)
        
        visit(node)
    ```

   - [Min-heap](): A complete binary tree where each node is smaller than its children. The root is the smallest element in the tree.
      Operations: `insert` and `extract_min`, both takes O(log n) time.
  
  - [Max-heap](): A complete binary tree where each node is larger than its children. The root is the largest element in the tree.
    Operations: `insert` and `extract_min`, both takes O(log n) time.
  
* [Red Black Trees](https://github.com/amandazhuyilan/Castro-Street/blob/master/Data-Structures/LinkedList.py)

* [Linked lists](https://github.com/amandazhuyilan/Castro-Street/blob/master/Data-Structures/LinkedList.py)
  - [Loop detecting](https://github.com/amandazhuyilan/Castro-Street/blob/master/Problems-and-Solutions/hasLoop.py): Uses          Floyd's hare-and-turtle algorithm, make a fast pointer that travels in two nodes at a time, and a slow pointer that            travels one node at a time. If there exists a loop in the linked-list, fast and slow will meet. 

<a name="Sorting_Algorithms"></a>
### Algorithms
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
- [Breadth First Search(BFS)](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/BFS.py)
  - Explore each neightbour before exploring any children. 
  - Preferred if want to find shortest path between two nodes, as we wish to stay close to the starting node as close as possible.
  - Can be implemented using recursive or queue.

- [Depth First Search(DFS)](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/DFS.py)
  - Start at root or selected node and explore each branch completely before moving on to next branch.
  - Preferred if want to visit all nodes in graph. Simpler compared to BFS.
  - Tree Traversals mentioned above are a form of DFS.

<a name="Problems_and_Solutions"></a>
## Problems and Solutions
1. [Two sums](https://github.com/amandazhuyilan/Castro-Street/blob/master/twoSums.py).

  Returns the indices of two numbers in the input array that add up to the target number.

  * Solution 1: Brute force, O(n<sup>2</sup>) 
  * Solution 2: Dictionary. O(n). Set buffer_dictionary[target-nums[i]] = i if nums[i] not in buffer dictionary.  
  
  `TEST_CASE = ([1,4,5,10,3], 7)`
  
  Output: `[1,4]`
  
2. [Is Unique](https://github.com/amandazhuyilan/Castro-Street/blob/master/isUnique.py).
  
  Checks if the characters in the input string is unique. O(n).
  
  Create a empty list and append the ASCII vaule for each character in string after checking if the ASCII value already     exists. If exists, return `False`, else return `True`

  
  `TEST_CASE = "abd"`
  
  Output: `True`
  
3. [URLify](https://github.com/amandazhuyilan/Castro-Street/blob/master/URLify.py).
  
  Replaces the space(s) of input string.
  
  `TEST_CASE = This is a string`
  
  Output: `This%20is%20%a%string`
  
4. [set Zeroes Matrix](https://github.com/amandazhuyilan/Castro-Street/blob/master/Problems-and-Solutions/setZeroMatrix.py).
  
  Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
  
  `TEST_CASE = [[1, 2, 3], [5, 6, 0]]`
  
  Output:`[1, 2, 0], [0, 0, 0]`
  
<a name= "Cheat_Sheets"></a>
### Cheat Sheets
  - [Big Oh](http://bigocheatsheet.com/)
  - [Time Complexity Cheat Sheet](https://www.packtpub.com/sites/default/files/downloads/4874OS_Appendix_Big_O_Cheat_Sheet.pdf)
  - [HTML](http://www.simplehtmlguide.com/cheatsheet.php)
  - Regex. [Interactive Tutorial](https://regexone.com/) and [Online Regex Testing](https://regex101.com/).
  - [How does the internet works?](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)
