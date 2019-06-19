## ISA (Instruction Set Architecture
- Refers to the actual programmer-visible instruction set,serves as a boundary between the software and the hardware.
- Nearly all ISAs are classified as general purpose register architectures, where the operands are either registers or memory location
- 

## [RISC VS. CISC](https://cs.stanford.edu/people/eroberts/courses/soco/projects/risc/risccisc/)
We use a simple `MULT` instruction to demonstrate how the two architecture systems differ.

### RISC (Reduced Instruction Set Computer)
RISC processors only use simple instructions that can be executed within one clock cycle. RISC reduces the cycles per instruction at the cost of the number of instructions per program.

RISC was not widely spread due to the presence of Intel, who had the resource to develop the CISC chips, and the improvements between the RISC and CISC chips were not great enough to persuade buyers to change technologies. Due to the mentioned reason, lack of software support also became a contributing reason of the RISC roadblock. 

`MULT` command is divided into 3 separate commands: `LOAD` (move data from memory to register), `PROD` which finds the product of the two operands, `STORE` which moves data from register to memory.
Because there is more lines of code, more RAM is needed to store the assembly level instructions. The compiler must also perform more work to convert a high-level langauge statement to code of this form.

However, because each RISC instruction takes one clock cycle to execute, the entire program will execute the same amount of time as the multi-cycle CISC command that will be mentioned below. The RISC "reduced instructions" require less transistors of hardware space than the complex instructions, leaving more room for general purpose registers. And also because all of the instructions execute in one clock cycle, pipelining is possible.

Separating the `LOAD` and `STORE` command instructions helps reduce the amount of work that the computer must perform. After a CISC `MULT` is performed, the processors erases the registers. therefore if one of the operands needs to be used for another computation, the processor must re-load the data from the memory into a register. In RISC, the operand will remain in the register until another value is loaded in its place.

- Emphasis on software.
- Single-clock, reduced instruction only.
- Register-to-register: `LOAD` and `STORE` are independent instructions
- Low cycles per seconds, large code size
- Spends more transistors on memory registers

 ## CISC (Complex Instruction Set Computers)
The primary goal of CISC architecture is to complete a task in as few lines of assembly as possible. This is achieved by building processor hardware that is capable of understanding and executing a series of operations.

When executing the `MULT` instruction, this instruction loads the two values into separate registers, multiplies the operands in the execution unit, and then stores the product in the appropriate register. Thus, the entire task of multiplying two numbers can be completed with one instruction.

MULT is what is known as a "complex instruction." It operates directly on the computer's memory banks and does not require the programmer to explicitly call any loading or storing functions. It closely resembles a command in a higher level language. 

One of the primary advantages of this system is that the compiler has to do very little work to translate a high-level language statement into assembly. Because the length of the code is relatively short, very little RAM is required to store instructions. The emphasis is put on building complex instructions directly into the hardware.

- Emphasis on hardware
- Includes multi-clock complex instruction
- Memory-to-memory: `LOAD` and `STORE` incorporated in instructions
- Small code size, high cycles per second
- Transistors used for storing complex instructions.

The CISC approach attempts to minimize the number of instructions per program, sacrificing the number of cycles per instruction.

## Threads and Processes
### Process
Process is a progam loaded into memory, identified by a process id (`pid`), owns resources such as memory (code and data), open files, identity (user id, group id), timers etc. Resources owned by one process are protected from other resources.
- Processes are the building block components of a system
  - visible to each other
  - communicate with each other

### Thread
Thread is a single flow of execution or control, they are are implementation details of a process that are hidden inside processes. A thread has the following attributes, all of them have to do with running code:
- blocked and runnable states
  - blocked: waiting on something to happen: `REPLY` blocked on a IPC reply, `MUTEX` blocked on a wating for a mutex to be free, `RECEIVE` blocked on waiting to get a message.
    - most threads spend most of their time blocked - that's how CPU is shared between threads.
  - runnable: capable of using the CPU
  - two main ready states:
    - `RUNNING` actually using the CPU
    - `READY`: waiting while another thread is running
    
- priority
- scheduling algorithm
- register set
- CPU mask for multicore
- signal mask

Threads run in a process:
- a process must have at least one thread
- threads in a process share all the process resources
- _Threads run code, processes own resources_


### Reading List
[Execellent slides on implementation of mutex, condvars and semaphores by QNX](https://github.com/amandazhuyilan/Castro-Street/blob/master/04_nto_thread_r16.pdf)
