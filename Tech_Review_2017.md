# Technical Review Notes
Credits for _Cracking the Code Interview, 6th edition_ and _Data Structure and Algorithms in Python_. 

## Good code
Need to pass [CWE MITRE top 25](http://cwe.mitre.org/top25/) errors.

## Time/Space Complexity

### Big-O, Big-Ω, Big-Θ and Little-O
- T(n) is O(f(n)) = growth rate of T(n) <= growth rate of f(n) _Upper Bound_
- T(n) is Ω(f(n)) = growth rate of T(n) >= growth rate of f(n) _Lower Bound_
- T(n) is Θ(f(n)) = growth rate of T(n) == growth rate of f(n)f(n) _Exact Bound_
- T(n) is o(f(n)) = growth rate of T(n)T(n) < growth rate of f(n)f(n) _Upper Bound that does not equal to_

An __in-place__ algorithm operates directly on its input and changes it, instead of creating and returning a new object. 

### Hash Tables
Hash tables are used to associate key with values, each key should be able to compute a "hash function", which takes some or all information and digests it into a single integer.

Collision could be solved by using a linked-list.

Insertion, removal and lookup takes O(1) time, worst case takes O(n) time.

- Example: Use hash table to find all valid anagrams for a string:
  - Sort the strings alphabetically.
  - Add the sorted letters as a key in the table and the original word as one of the values in table.
  - For strings from input, sort them and lookup the keys in the table, add if not exists or add to value if exists.
  - Runs in O(n log n) for sorting and O(1) for lookup.
  
 
### ASCII and UNICODE 
ASCII defines 128 characters,mapping to 0-127 characters. Unicode defines 2<sup>21</sup> characters.
Unicode is a superset of ASCII, and the numbers 0–128 have the same meaning in ASCII as they have in Unicode.

Because Unicode characters don't generally fit into one 8-bit byte, there are numerous ways of storing Unicode characters in byte sequences, such as UTF-32 and UTF-8.

### Binary Search Trees
- BST Operations are usuallty O(log n). 
- Can be implemented as Hash table by storing <key, value> pairs and order nodes based on keys.

Shortest path between two nodes in a BST: Find the _lowest common ancestor_.
- Keep track of the start node and destination node in two sets.
- Move up the tree and find the parent of the node, store it in the same set correspondingly.
- The unique path is found once the entry to the two sets are identical.

#### Red Black Trees
Red Black trees is a balanced Binary Search tree with an extra bit per node-> makes a node either red or black.
- Every node is red or black
- Root is black
- Leaf is black
- If node is red then node is black
- For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.

- By constrainting the node colors on any path frpm the root to a leaf, RBT ensure that no such path is more then twice as ling as another.
- Has height of most 2log(n+1).
- Operations all costs O(log n).

### Bitwise Operation
__Two's Complement__: Take the inverse of the binary form and add 1.
In Python:
- x << y => x shifting to the left by y places (multiplying by 2y).
- x >> y => x shifting to the right by y places (dividing by 2y).
- x & y  => bitwise AND.
- x | y  => bitwise OR.
- x      => returns the complement of x. (-x - 1).
- x ^ y  => bitwise XOR. 

  
### Network
#### When you type a URL into a web browser, this is what happens:
- If the URL contains a domain name, the browser first connects to a domain name server and retrieves the corresponding IP address for the web server.
- The web browser connects to the web server and sends an HTTP request (via the protocol stack) for the desired web page.
- The web server receives the request and checks for the desired page. If the page exists, the web server sends it. If the server cannot find the requested page, it will send an HTTP 404 error message. 
- The web browser receives the page back and the connection is closed.
- The browser then parses through the page and looks for other page elements it needs to complete the web page. These usually include images, applets, etc.
- For each element needed, the browser makes additional connections and HTTP requests to the server for each element.
- When the browser has finished loading all images, applets, etc. the page will be completely loaded in the browser window.

### Computer Systems
Each __process__ has one or more __threads__, the processor switches between threads quickly, only one thread is running at given time. 

__Context Switching__: CPU storing and restoring the 
#### Mutex, Locks, Sepamore and monitor
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

#### Polymorphism
The ability of one method to have different behaviours depending on the type of object it is being called on or the type of object being passed as the parameter.

Example: the ```add``` function would result in different behaviour depending on the type of input(int/float/double and string)

#### [Heaps and Stacks](http://net-informations.com/faq/net/stack-heap.htm)
Stack is used for static memory allocation and heap for dynamic memory allocation, both stored in the computer's RAM .

- __Stack__

  Variables allocated on the stack are stored directly to the memory and access to this memory is therefore fast, and it's       allocation happens when the program is compiled. 
  When a function or a method calls another function which in turns calls another function etc., the execution of all those     functions remains suspended until the very last function returns its value. The stack is always reserved in a LIFO order,     the most recently reserved block is always the next block to be freed. This makes it really simple to keep track of the       stack, freeing a block from the stack is nothing more than adjusting one pointer.

- __Heap__

  Variables allocated on the heap have their memory allocated at run time and accessing this memory is a bit slower, but the     heap size is only limited by the size of virtual memory . Element of the heap have no dependencies with each other and can     always be accessed randomly at any time. You can allocate a block at any time and free it at any time. This makes it much     more complex to keep track of which parts of the heap are allocated or free at any given time.

  - Use stack if exactly how much data needed to allocate is known before compile time and it is not too big.	Use heap if       don't know exactly how much data needed at runtime or need to allocate a lot of data.

  - In a multi-threaded situation each thread will have its own completely independent stack but they will share the heap.        Stack is thread specific and heap is application specific. The stack is important to consider in exception handling and        thread executions.
  
#### Segmentation Fault
  A segmentation fault is when your program attempts to access memory it has either not been assigned by the operating system,   or is otherwise not allowed to access.
  
#### Stack Overflow
- When a particular computer program tries to use more memory space than the call stack has available.
- Happens during excessively deep or infinite recursion, in which a function calls itself so many times that the space needed to store the variables and information associated with each call is more than can fit on the stack. Can also happen when large stack variables are allocated.

