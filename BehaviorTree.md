## Behavior Trees

### Background

Behavior trees were first developed in computer games to control NPCs (Non-Player Characters), where in the gaming industry modularity is a key property
that enables reuse of code, incremental design of functionality and efficient testing.

Since behavior trees are, by defininition, non self referential in that the leaf nodes should never point back to the parent, it makes it very easy to: 
- decompose the task into simpler ones without being concerned about how the subtask will fit into the larger class.
- be reused in the context of another higher level behavior, without needing to specify how they relate to
the subsequent behaviors.

### What are Behavior Trees

Behavior Tree is a directed root tree that consists of 3 types of nodes: _controlled flow nodes_ ("behavior"), a _state odifying node_ ("decorator") and leaf nodes, _execution nodes_, that does the actual work.

A behavior tree starts its __Depth First Traversal__ execution from the root node that generates signals to allow the execution of a node called _tick_ with a given frequency, which are sent to its children nodes.

A node is executed only and only if it receieved a tick. The child node withh immediately return _RUNNING_ to
the parent, _SUCCESS_ if the goal is reached, or _FAILURE_ otherwise.

### Finite State Machines (FSM)
An Finite State Machine is defined by a list of its states, its initial state, and the conditions for each transition.

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
