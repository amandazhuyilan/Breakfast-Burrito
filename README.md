# Technical Review Notes
### Table of Contents
[Clean and Good Code?](#Clean_Code)

[Time Complexity](#Time_Complexity)


Data Structure and Algorithms
  - [Hash Tables](#Hash_Tables)
  - [ASCII and UNICODE](#ASCII_and_UNICODE)
  - [Binary Search](#Binary_Search)
  - [Binary Search Trees](#Binary_Search_Trees)
  - [Graphs](#Graphs)
  - [Linked List](#Linked_List)
  - [Heap and Priority Queues](#Heap_and_Priority_Queues)
  - [Queues and Stacks](#Queues_and_Stacks)
  - [Algorithms](#Algorithms)
  - [Bitwise Operations](#Bitwise_Operations)
  - [Iteration and Recursion](#Iteration_and_Recursion)
  
[Network](#Network)

[Computer Systems Knowledge](#Computer_Systems)
  - [Mutex, Locks, Sepamore and Monitor](#mutex)
  - [Polymorphism](#Polymorphism)
  - [Heaps and Stacks](#Heaps_and_Stacks)
  - [Memory Layout Diagrams](#Memory_Layout)
  - [Common Errors](#Common_Errors)
    - [Segmentation Fault](#Segmentation_Fault)
    - [Buffer Overflow](#Buffer_Overflow)
    - [Memory Leak](#Memory_Leak)
    - [Stack Overflow](#Stack_Overflow)
    
[Cheat Sheets](#Cheat_Sheets)  

Python main template:
```python 
#!/usr/bin/env python

def main():
    """ Main program """
    # Code goes over here.
    return 0

if __name__ == "__main__":
    main()
```

<a name="Clean_Code"></a>
### Clean and Good Code?
Written by someone who cares.

Need to pass [CWE MITRE top 25 errors.](http://cwe.mitre.org/top25/) 

- __Single Responsibility Principle__. A function should be responsible for a single aspect of a system's requirements，which can be changed independently of other aspects. Should have minimal dependencies.

- __Don't Repeat Yourself__. The modification of any single element of a system doesn't require a change in any other logically unrelated elements.

- __Keep It Simple and Stupid__. Most system works best if they are kept simple rather than made complex.

- Can be easily extended by any other developer. Be mindful and considerate. You might be the "other debveloper" some day.

- Should have unit and acceptance tests.

<a name="Time_Complexity"></a>
## Time/Space Complexity

Metrics used to descripe the efficiency of algorithms.

### Big-O, Big-Ω, Big-Θ and Little-O
- T(n) is O(f(n)) = growth rate of T(n) <= growth rate of f(n) _Upper Bound_
- T(n) is Ω(f(n)) = growth rate of T(n) >= growth rate of f(n) _Lower Bound_
- T(n) is Θ(f(n)) = growth rate of T(n) == growth rate of f(n)f(n) _Exact Bound_
- T(n) is o(f(n)) = growth rate of T(n)T(n) < growth rate of f(n)f(n) _Upper Bound that does not equal to_

An __in-place__ algorithm operates directly on its input and changes it, instead of creating and returning a new object. 

<a name="Hash_Tables"></a>
### Hash Tables
Hash tables are used to associate key with values, each key should be able to compute a "hash function", which takes some or all information and digests it into a single integer.

Collision could be solved by using a linked-list.

Insertion, removal and lookup takes O(1) time, worst case takes O(n) time.

- Example: Use hash table to find all valid anagrams for a string:
  - Sort the strings alphabetically.
  - Add the sorted letters as a key in the table and the original word as one of the values in table.
  - For strings from input, sort them and lookup the keys in the table, add if not exists or add to value if exists.
  - Runs in O(n log n) for sorting and O(1) for lookup.
  
<a name="ASCII_and_UNICODE"></a>
### ASCII and UNICODE 
ASCII defines 128 characters,mapping to 0-127 characters. Unicode defines 2<sup>21</sup> characters.
Unicode is a superset of ASCII, and the numbers 0–128 have the same meaning in ASCII as they have in Unicode.

Because Unicode characters don't generally fit into one 8-bit byte, there are numerous ways of storing Unicode characters in byte sequences, such as UTF-32 and UTF-8.


<a name="Binary_Search"></a>
### Binary Search

Let's assume we want to find a target number in an array of ints in ```nums```:

```python
def BinarySearch(self, startIndex, endIndex, nums, target):
  while startIndex + 1 < endIndex:
    mid = (startIndex + endIndex)//2
    if nums[mid] == target:
      return True
    elif nums[mid] > target:
      return self.BinarySearch(startIndex, mid - 1, nums, target)
    elif nums[mid] < target:
      return self.BinarySearch(mid + 1, endIndex, nums, target)
  return False
  ```
  
<a name="Binary_Search_Trees"></a>
### [Binary Search Trees](https://github.com/amandazhuyilan/Castro-Street/blob/master/Data-Structures/BinarySearchTree.py)
  - A binary search tree is a binary tree in which all left decendents <= n <= all right decendents.
  - BST Operations are usuallty O(log n). The length of a balanced BST is log n, worst case scenario is n.
  - Complete binary tree: every level is filled except for perhaps the last level.
 
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
    
<a name="Graphs"></a>
### Graphs 

Constructing a graph in an adjacency list format with ```defaultdict``` (imported from ```collections```) when adding an edge for not existing vertex, this will not throw KeyError exception like the normal dictionary function, but will just create a new vertex along with this edge.
  
  - BFS for graphs: By implementing a queue and a ```visited``` list to keep track of if the nodes of a vertex, starting with the source, BFS prints out the neighbouring nodes of the vertex and moves on to the next one by popping the queue.
  
  - DFS for graphs: Using a recrusive function in the ```DFS_helper``` function, we go down the vertex starting from the source and prints all the vertices that are not included in the ```visited``` list.
  
  - [Graphs with python ```dict``` structures](https://github.com/amandazhuyilan/Castro-Street/blob/master/Problems-and-Solutions/FindPath.py)

    
    
<a name="Linked_List"></a>
### Linked List 

#### [Linked lists](https://github.com/amandazhuyilan/Castro-Street/blob/master/Data-Structures/LinkedList.py)
  - [Loop detecting](https://github.com/amandazhuyilan/Castro-Street/blob/master/Problems-and-Solutions/hasLoop.py): Uses          Floyd's hare-and-turtle algorithm, make a fast pointer that travels in two nodes at a time, and a slow pointer that            travels one node at a time. If there exists a loop in the linked-list, fast and slow will meet. 
  
<a name="Heap_and_Priority_Queues"></a>
### Heap and Priority Queues
```
                    Heap        PriorityQueue
1. Insert()         logn           logn
2. Delete()         logn           O(n)/ X
3. Pop()            logn           logn
4. Find()           logn             X
5. Modify()         logn             X
6. Min / Max        O(1)           O(1)
7. upper / lower     X              X
```

<a name="Queues_and_Stacks"></a>
### Queues and Stacks
BFS uses queue, DFS uses stack.
#### Stacks
LIFO. Used for tracing back to previous elements or operations.
```
class Stack:
    def __init__(self):
        self.stack = []
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    def push(self,val):
        return self.stack.append(val)
    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return self.size() == 0
```
#### Queues
FIFO. Often used in BFS or implementing caches.
```
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,val):
        self.queue.insert(0,val)
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()
    def size(self):
        return len(self.queue)
    def is_empty(self):
        return self.size() == 0
```
#### Implementing Stacks using Queues
__Method 1__ (By making push operation costly):
```
push(s, x)          // x is the element to be pushed and s is stack
  1) Enqueue x to q2
  2) One by one dequeue everything from q1 and enqueue to q2.
  3) Swap the names of q1 and q2 
// Swapping of names is done to avoid one more movement of all elements 
// from q2 to q1. 

pop(s)
  1) Dequeue an item from q1 and return it.
```

__Method 2__ (By making pop operation costly):
```
push(s,  x)
  1) Enqueue x to q1 (assuming size of q1 is unlimited).

pop(s)  
  1) One by one dequeue everything except the last element from q1 and enqueue to q2.
  2) Dequeue the last item of q1, the dequeued item is result, store it.
  3) Swap the names of q1 and q2
  4) Return the item stored in step 2.
// Swapping of names is done to avoid one more movement of all elements 
// from q2 to q1.
```
#### Implementing Queues using Stacks
__Method 1__ (By making enQueue operation costly)
```
enQueue(q, x)
  1) While stack1 is not empty, push everything from stack1 to stack2.
  2) Push x to stack1 (assuming size of stacks is unlimited).
  3) Push everything back to stack1.

deQueue(q)
  1) If stack1 is empty then error.
  2) Pop an item from stack1 and return it
```

__Method 2__ (By making deQueue operation costly)
```
enQueue(q,  x)
  1) Push x to stack1 (assuming size of stacks is unlimited).

deQueue(q)
  1) If both stacks are empty then error.
  2) If stack2 is empty
       While stack1 is not empty, push everything from stack1 to stack2.
  3) Pop the element from stack2 and return it.
```
<a name="Algorithms"></a>
### Algorithms

#### Sorting Algorithms
* [Counting Sort](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/CountingSort.py)
  
  Sorting on O(n). Uses an auxiliary array that holds the number of elememts that equal to the index of Index_Arr. 
  Based on the number of entires specified in the Index_Arr, the Out_Arr stores the sorted array in an ascending order.
  
* [Heap Sort](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/HeapSort.py)

* [Quick Sort](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/QuickSort.py)

  In-place and non-in-place methods included. Sorts in O(n log n).

* [Insertion Sort](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/InsertionSort.py)

  An efficient algorithm for sorting a small number of elements. Time complexity: Best O(n), Worst: O(n<sup>2</sup>).

* [Merge Sort](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/MergeSort.py)

  A divide, conquer and combine recursive sorting algorithm. Time complexity: O(n log(n)).
  
#### Searching Algorithms 
- [Breadth First Search(BFS)](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/BFS.py)
  - Explore each neightbour before exploring any children. 
  - Preferred if want to find shortest path between two nodes, as we wish to stay close to the starting node as close as possible.
  - Can be implemented using recursive or queue.

- [Depth First Search(DFS)](https://github.com/amandazhuyilan/Castro-Street/blob/master/Algorithms/DFS.py)
  - Start at root or selected node and explore each branch completely before moving on to next branch.
  - Preferred if want to visit all nodes in graph. Simpler compared to BFS.
  - Tree Traversals mentioned above are a form of DFS.

<a name="Bitwise_Operations"></a>  

### Bitwise Operations
__Two's Complement__: Take the inverse of the binary form and add 1.
In Python:
- x << y => x shifting to the left by y places (multiplying by 2y).
- x >> y => x shifting to the right by y places (dividing by 2y).
- x & y  => bitwise AND.
- x | y  => bitwise OR.
- x      => returns the complement of x. (-x - 1).
- x ^ y  => bitwise XOR. 


<a name="Iteration_and_Recursion"></a>
### Iteration and Recursion

Both perform the same kinds of tasks: Solve a complicated task one piece at a time, and combine the results. 

- Iteration: keep repeating until a task is “done”.
  - e.g., loop counter reaches limit, linked list reaches null pointer, instream.eof() becomes true. 
  
- Recursion: solve a large problem by breaking it up into smaller and smaller pieces until you can solve it; combine the results.
  - e.g., recursive factorial funtion


<a name="Network"></a>  
### Network
#### When you type a URL into a web browser, this is what happens:
- If the URL contains a domain name, the browser first connects to a domain name server and retrieves the corresponding IP address for the web server.
- The web browser connects to the web server and sends an HTTP request (via the protocol stack) for the desired web page.
- The web server receives the request and checks for the desired page. If the page exists, the web server sends it. If the server cannot find the requested page, it will send an HTTP 404 error message. 
- The web browser receives the page back and the connection is closed.
- The browser then parses through the page and looks for other page elements it needs to complete the web page. These usually include images, applets, etc.
- For each element needed, the browser makes additional connections and HTTP requests to the server for each element.
- When the browser has finished loading all images, applets, etc. the page will be completely loaded in the browser window.

<a name="Computer_Systems"></a>
### Computer Systems Knowledge
Each __process__ has one or more __threads__, the processor switches between threads quickly, only one thread is running at given time. 

<a name="mutex"></a>
#### Mutex, Locks, Sepamore and Monitor
- __Mutex__

  An OS program object (counter) to allow multiple program thread to take turns sharing the same resource.
  - Usually an int = 1.
  - When thread locks mutex, mutex -= 1, when thread unlocks mutex, mutex += 1.

- __Semaphore__

An OS program object (counter) that may start off greater than 1. A binary semaphore is a mutex.
- Number of threads allowed to access resource at once = starting int of semaphores.
- Support "wait" ("lock") and "signal" ("unlock") operations.

- __Monitor__

A user-defined object/class designed for multiple thread access. Special type of semaphore. If one thread is currently executing a member function of the object then any other thread that tries to call a member function of that object will have to wait until the first has finished.
  

Mutex Structures:  
  - Single-core:
  ```
  bool Locked = False      // determine if lock is locked/unlocked
  queue waitlist           // list of process/threads to be run
  ```
  
  - Multi-cores: 
  ```
  int spinlock            // a lock which causes a thread trying to acquire it to simply wait in a loop ("spin") while                                     repeatedly checking if the lock is available. 
  bool Locked = False     
  queue waitlist          
  ```
__Deadlocks__

A situation when a thread is waiting for an object lock that another thread holds, and this second thread is waiting for the an object that the first thread holds. They both remain waiting forever. This can happen under the following situation:
  1. Mutual Exclusion: There a limit access to resources.
  2. Hold and Wait: Processes already holding a resource can request additional resources, without relinquishing their current      resources. 
  3. No Preemption: One process cannot force another process to remove their access to the resource.
  4. Circular Wait: Two or more processes form a circular chain where each process is waiting on another resource in the                           chain.
Deadlock prevention: Locks ranking.

<a name="Polymorphism"></a>
#### Polymorphism
The ability of one method to have different behaviours depending on the type of object it is being called on or the type of object being passed as the parameter.

Example: the ```add``` function would result in different behaviour depending on the type of input(int/float/double and string)

<a name="Memory_Layout"></a>
#### Memory Layout Diagram
![Memory Layout](http://static.duartes.org/img/blogPosts/linuxFlexibleAddressSpaceLayout.png)
![Memory Layout from class](https://github.com/amandazhuyilan/Castro-Street/blob/master/Memory%20Layout.JPG)

<a name="Heaps_and_Stacks"></a>
#### [Heaps and Stacks](http://net-informations.com/faq/net/stack-heap.htm)
Stack is used for static memory allocation and heap for dynamic memory allocation, both stored in the computer's RAM .

Use stack if exactly how much data needed to allocate is known before compile time and it is not too big.	Use heap if don't know exactly how much data needed at runtime or need to allocate a lot of data.

- __Stack__

The most straightforward way LIFO stacks may be programmed into conventional computers is to allocate an array in memory, and keep a variable with the array index number of the topmost active element. Blocks of memory locations can be allocated and a pointer (%esp) with the actual address of the top stack element is used to maintain and keep track of the topmost element.

A very important property of stacks is that, in their purest form, they only allow access to the top element in the data structure. They allow recursive invocations of procedures without risk of destroying data from previous invocations of the routine.

Variables allocated on the stack are stored directly to the memory and access to this memory is therefore fast, and it's       allocation happens when the program is compiled. 

The stack is always reserved in a LIFO order, the most recently reserved block is always the next block to be freed. This makes it really simple to keep track of the stack, freeing a block from the stack is nothing more than adjusting one pointer.

- __Heap__

Variables allocated on the heap have their memory allocated at run time and accessing this memory is a bit slower, but the     heap size is only limited by the size of virtual memory . Element of the heap have no dependencies with each other and can     always be accessed randomly at any time. You can allocate a block at any time and free it at any time. This makes it much     more complex to keep track of which parts of the heap are allocated or free at any given time.

  - In a multi-threaded situation each thread will have its own completely independent stack but they will share the heap.        Stack is thread specific and heap is application specific. The stack is important to consider in exception handling and        thread executions.

The following content is taken out from [_Operating Systems: Three Easy Pieces_](http://pages.cs.wisc.edu/~remzi/OSTEP/#book-chapters) by Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau.

<a name="Common_Errors"></a>
### Common Errors

<a name="Segmentation_Fault"></a>
#### Segmentation Fault
An error caused when not allocating memory for some routines calls which requires ```malloc()```. 

<a name="Buffer_Overflow"></a>
#### Buffer Overflow
A related error for not allocating enough memory. In some cases this is harmless, perhaps
overwriting a variable that isn’t used anymore. In some cases, these over-
flows can be incredibly harmful, and in fact are the source of many security
vulnerabilities in systems.

<a name="Memory_Leak"></a>
#### Memory leak
Happens when memory that is allocated, then unused but never freed. The device should work indefinitely, without ever needing a reboot, but this will slowly leak memory eventually
leads to running out of memory, at which point a restart is required.

<a name="Stack_Overflow"></a>  
#### Stack Overflow
When a particular computer program tries to use more memory space than the call stack has available.

Happens during excessively deep or infinite recursion, in which a function calls itself so many times that the space needed to store the variables and information associated with each call is more than can fit on the stack. Can also happen when large stack variables are allocated.

<a name= "Cheat_Sheets"></a>
### Cheat Sheets
  - [Big Oh](http://bigocheatsheet.com/)
  - [Time Complexity Cheat Sheet](https://www.packtpub.com/sites/default/files/downloads/4874OS_Appendix_Big_O_Cheat_Sheet.pdf)
  - [HTML](http://www.simplehtmlguide.com/cheatsheet.php)
  - [Online Regex Testing](https://regex101.com/).
  - [How does the internet works?](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)
  - [MIT Handouts _Hacking a Google Interview](http://courses.csail.mit.edu/iap/interview/materials.php)

