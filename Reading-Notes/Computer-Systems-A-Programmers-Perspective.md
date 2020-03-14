### Note from *Computer System, A Programmer's Perspective* (Third Edition)


#### Chap. 1 A Tour of Computer Systems
- How a compiler (`GCC`) reads and translate a source file (`hello.c`) to an executable object (`hello`):

  - `hello.c` -[pre-processor `cpp`]-> `hello.i`(modified source program, text) -[Compiler `ccl`]->`hello.s`(assembly program, text)-[Assembler `as`]->`hello.o`(relocatable object program, binary)-[Linker `ld`]->`hello`(executable object program, binary)

- **Buses** - a collection of electrical conduits that carry information back and forth between components. They are designed to transfer **fixed sized chunk of bytes** (known as words), usually in 4 bytes (32 bits) or 8 bytes (64 bits). 
- **I/O Devices** - the system's connection to the external world. They are connected to the I/O bus by either a *controller* (chip sets in the device itself or on the motherboard),
or on an *adapter*(a card that plugs into a slot on the motherboard).
- **Processor (CPU)** - the engine that interpretes or executes the instructions stored in the main memory. It contains the PC (Program Counter) that points at the address of some machine-language instruction from main memory.

   Here's what the processor does repeatedly since it's turned on:

  - reads the instruction from the memory pointed at by the PC, 
  - interprets the bits in the instruction,
  - performs some simple operations dictated by the instruction,
    - sequence of operations determined by instruction execution model set by Instruction Set Architecture,
    - involving ALU (Arithmetic Logic Unit), main memory and register file 
  - updates the PC to point to the next instruction.
  
 - **Operating System** - the layer of software interposed between the application program and the hardware. Two main purposes:
   - to protect the hardware from misuse by runaway applications
   - to provide applications with simple and uniform mechanisms for manipulating complicated and often wildly different low-level hardware devices.
   
 - **Processes** - the operating system's abstraction for running a program.
   - A single CPU can appear to execute multiple processes concurrently by having the processor switch among them by *context switching*.
   
 - **Kernel** - the portion of the operating system code that is always resident in memory. 
   - A *collection of code and data structure* that the system uses to manage all the processes.
   - When an application program requires some action by the operating system, such as to read/write a file, it executes a system call instruction, transferring control to the kernel.

- **Threads** - multiple execution units that make up a process. They each run in the context of the process and share the same code and global data.
- **Heap** and **Stack** - 
  - both exists in process virtual address space. 
   - both expand and contract dynamically at run times
      - [Heap] as a result to `malloc` and `free`.
      - [Stack] due to complier implementing function calls.
- **Amdahl's Law** - when we speed up one part of the system, the effect on the overall system performance depends on both:
  - how significant this part of the system is to the overall system
  - how much it sped up.
- **Concurrency and Parallelism**
  - **Multi-core processors** integrated onto a single-integrated chip, each core has its own L1 and L2 cache and a shared L3 cache between all cores.
  - **Hyperthreading** - allows single CPU to execute multiple flows of control, by having multiple copies of some of the CPU hardware, such as Program Counter and Register Files,
 while having only single copies of other parts of the hardware.
 
 - **Abstractions in Computer Systems**
   - [Processor] *Instruction Set Architecture* provides an abstraction of the actual processor hardware.
     - A machine-code program behaves as if it were executed on a processor that performs one instruction at a time.
   - [OS] *Files* as an abstraction of I/O devices,
   - [OS] *Processes* as an abstraction of a running program,
   - [OS] *Virtual Machine* as an abstraction to the entire computer.

#### Chap. 2 Representing and Manipulating Information
- **Hexadecimal Notation** is used to conveniently describe bytes (8 bits). Binary notation is too verbose, decimal notation is too tedious to convert to and back from.

- **Word Sizes** indicate the size of pointer data. The most important system parameter determined by the word size is the maximum size of the _virtual_ address space. 32-bit word size limit the virtual address space to 4GB, while a 64-it word size leads to a virtual address space of 16 exabytes (2^60) bytes.

- **Little & big endian** - for an int that has a hexadecimal value of `0x012345` at address `0x100`:
  - Big endian: most significant byte comes first - [`0x100`] -> `01`, [`0x101`]->`23`, [`0x102`]->'45', IBM, Oracle.
  - Little endian: least significant byte comes first - [`0x100`] -> `45`, [`0x101`]->`23`, [`0x102`]->'01', Windows & Linux, Intel, Andriod & IOS.

- **Shift Operations in C**
  - Logical shift: A logical right shift fills in the left end with `k` zeros. [For **unsigned data**]
  - Aritmetic shift: An arithmetic right shift fills the in left end with `k` repetition with the most significant bit.
  - Shifts have lower precedence than shifts - `1<<2 + 3 << 4 => 1 << (2 + 3) << 4.

