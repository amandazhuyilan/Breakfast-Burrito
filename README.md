
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
* [Graphs](https://github.com/amandazhuyilan/Castro-Street/blob/master/Data-Structures/graph.py)

  Constructing a graph in an adjacency list format with ```defaultdict``` (imported from ```collections```) when adding an edge for not existing vertex, this will not throw KeyError exception like the normal dictionary function, but will just create a new vertex along with this edge.
  
  - BFS for graphs: By implementing a queue and a ```visited``` list to keep track of if the nodes of a vertex, starting with the source, BFS prints out the neighbouring nodes of the vertex and moves on to the next one by popping the queue.
  
  - DFS for graphs: Using a recrusive function in the ```DFS_helper``` function, we go down the vertex starting from teh source and prints all the vertices that are not included in the ```visited``` list.
  
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
  
2. [Is Unique](https://github.com/amandazhuyilan/Castro-Street/blob/master/isUnique.py).
  
3. [URLify](https://github.com/amandazhuyilan/Castro-Street/blob/master/URLify.py).
 
4. [set Zeroes Matrix](https://github.com/amandazhuyilan/Castro-Street/blob/master/Problems-and-Solutions/setZeroMatrix.py).
  
5. [SurroundedRegions](https://github.com/amandazhuyilan/Castro-Street/blob/master/Problems-and-Solutions/SurroundedRegions.py)

  
<a name= "Cheat_Sheets"></a>
### Cheat Sheets
  - [Big Oh](http://bigocheatsheet.com/)
  - [Time Complexity Cheat Sheet](https://www.packtpub.com/sites/default/files/downloads/4874OS_Appendix_Big_O_Cheat_Sheet.pdf)
  - [HTML](http://www.simplehtmlguide.com/cheatsheet.php)
  - Regex. [Interactive Tutorial](https://regexone.com/) and [Online Regex Testing](https://regex101.com/).
  - [How does the internet works?](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)
  - [MIT Handouts _Hacking a Google Interview-](http://courses.csail.mit.edu/iap/interview/materials.php)
