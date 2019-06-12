## Behavior Trees

### How did Behavior Trees come along

Behavior trees were first developed in computer games to control NPCs (Non-Player Characters), where in the gaming industry modularity is a key property
that enables reuse of code, incremental design of functionality and efficient testing.

- In Robotic Manipulation, the __main advantage__ of using Behavior Trees are that they can be easily reused in the context of another higher level behavior, without needing to specify how they relate to
the subsequent behaviors.

- In robot programming of pick-and-place operations, behavior trees allow end-users to visually create programs with the same amount of complexity and power
as traditionally-written programs.

- In brain surgery robots, behavior trees are favoured due to their flexibility, reusability and simple syntax.

### What are Behavior Trees

Behavior Tree is a directed root tree where the internal nodes are called _controlled flow nodes_ and leaf nodes are called _execution nodes_.
A behavior tree starts its execution from the root node that generates signals to allow the execution of a node called _tick_ with a given frequency, 
which are sent to its children nodes. A node is executed only and only if it receieved a tick. The child node withh immediately return _RUNNING_ to
the parent, _SUCCESS_ if the goal is reached, or _FAILURE_ otherwise.

### Finite State Machines (FSM)
Advantages:
- Common structure, intuitive and easy to understand and implement.
- Ideal for simple, less complex systems.

Disadvantages:
- Maintainability: Adding or removing states requires the re-evaluation a potentially large number of transitions and internal states of the FSM.
     - After adding a new state, each existing transition must be re-evaluated (possibly removed or replaced) and new transitions from/to the new state must be evaluated as well.
                   This makes FSMs highly susceptible to human design errors and impractical from an automated design perspective.
- Scalability: FSMs with many states and many transitions between them are hard to modify, for both humans and computers.
- Reusability: The transitions between states may depend on internal variables, making it unpractical to reuse the same sub-FSM in multiple projects.

#### Conversation between FSM and BT
![Alt text](bt-fsm.png?raw=true "Optional Title")

To translate a FSM design to a BT, the most straight forward way is to create a global State Variable available to all parts of the BT and then list all the states of the FSM and their corresponding transitions and actions.
![Alt text](fsm-bt.png?raw=true "Optional Title")
