# {OS} 1. Introduction to Operating System

Course: Operating Systems
Confidence: Not Confident
Materials: intro_and_types_of_OS.pptx
Last Edited: September 9, 2024 11:11 PM

> 1. Program 
                   —|| Inbuilt / Installed in the system ||—
                   Run/Open
2. Process
> 

# Operating System

- Set of programs which act as an interface b/w UI & computer hardware & controls the execution of all kind of programs

### Functions

Memory Management

---

File Management

---

Job Accounting

---

Processor Management

---

Security

---

Error Detecting Aids

---

Device Management

---

Ctrl System Performance

---

Coordination b/w other software & users

---

### Roles

### User View

- Ease of use
- Resource Utilization

### System View

### Programs

**System Program (** Not part of Kernel **)**

**Application Program**

**Kernel**

---

- July 29, 2024
    
    # Evolution of Operating System
    
    ## First Generation ( 1945 - 1955 )
    
    - No OS existed
    - Vacuum Tubes
    - Punch Cards ( Magnetic Tapes / Cards )
    - Operator
    - Offline Mode
    - Consumed More Electricity; More Heat Generated
    - No protection
    
    - Plug Boards
    
    ## Second Generation ( 1955 - 1965 )
    
    - GMOSIS
    - For IBM, GM created it
    - Because it gathers all related jobs into groups ( batches ) & then submits them to the OS using a punch card to finish all of them
        - Built on a single stream batch operating system
    - Transistors were used
    - There was minimum protection
    - I/O operation-processor had to remain IDLE
    - Base for multi-progmamming
    
    ## Third Generation ( 1965 - 1980 )
    
    - Multi programming & multi tasking
    - Integrated Circuits ( IC ) were used
    - No starvation
    
    ## Fourth Generation ( 1980 - Present )
    
    - Development of Microsoft & Windows OS.
    - Provided GUI
    - No Starvation
    - Maximum CPU Utilisation
    - Computer Networking
    - Provides High Priority Execution
- July 31, 2024
    
    # Types of Operating Systems
    
    1. Batch-idle
    2. Multi-programmed
        - Non pre-emptive-complete execution process
        - Less-idleness
    3. Multi-tasking / time-sharing-responsive
        - Preemptive
        - Cooperative
    4. Real time OS ( YouTube )
        - No delay
        - Hard-Live
        - Soft-Delayed
    5. Distributed
        - Many networks-global
    6. Clustered
        - One network/global
    7. Embedded
        - Fixed Functionalities
    
    ---
    
    ### Batch Operating System
    
    - Doesn’t interact with computer directly
    - Operator takes similar jobs with similar requirements & groups into **batches**
    
    > Designed to manage & execute large no: of jobs efficiently by processing them into groups
    > 
    
    ### Advantages
    
    - **Multiple users** share same batch system
    - **Idle time** is very less
    - Easy to manage **large work repeatedly**
    
    ### Disadvantages
    
    - Hard to **debug**
    - Initial setup is **costly**
    - Other jobs wait for unknown amount of time if any job fails
    - Processing time for jobs is hard to accurately predict when in queue
    
    ---
    
    ### Multi-Programming Operating System
    
    <aside>
    ❓ All jobs to be done will be added into RAM
    ~~CPU will execute one job completely before staring to execute the next one~~
    
    If process want to do something else ( I/O ), CPU can go to other job to execute. This is the main concept of multi-programming
    
    </aside>
    
    - > 1 program can be present in main memory
    - Any one of them can be kept in execution
    
    ---
    
    - In a **Multiprogramming Environment** when a process does its I/O
        - CPU can start execution of other processes
    
    ---
    
    ### Advantages
    
    - Increases **throughput** of system
    - Reduces **response time**
    
    ### Disadvantages
    
    - **No facility for** **user interaction** of system resources within the system
    
    ---
    
    ### Multi-Tasking Operating System
    
    - Multi-programming OS with a facility of having the
        - ***ROUND-ROBIN SCHEDULING ALGORITHM***
    - Can run multiple programs simultaneously
    - Allows user to perform > 1 computer task at the same time
    
    ---
    
    - **Types**
        - Preemptive Multi-Tasking
        - Cooperative Multi-Tasking
    
    ---
    
    ### Advantages
    
    - **Multiple programs** can be executed simultaneously
    - Proper **memory management**
    
    ### Disadvantages
    
    - System gets heated in case of **heavy programs** multiple times
    
    ---
    
    ### Time-Sharing Operating System
    
    - Each task is given some time to execute
        - So that all tasks work smoothly
    
    <aside>
    ❓ A.K.A MULTI-TASKING OPERATING SYSTEM
    
    </aside>
    
    ### Quantum - time that each task gets to execute
    
    - After time interval is over, OS switches over to the next task
    
    ---
    
    ### Advantages
    
    - Each task gets **equal opportunity**
    - Fewer chances of **duplication of software**
    - **CPU idle time** is reduced
    - Resource Sharing, Improved Productivity, Improved UX
    
    ### Disadvantages
    
    - **Reliability**
    - Must take care of **security & integrity** of user programs & data
    - **Data communication**
    - High Overhead, Complexity, Security Risks
    
    ---
    
    ### Multi-Processing Operating System
    
    - > 1 CPU is used for execution of resources
    - ***Parallel Computing***  is achieved
        - > 1 processors present in the system can execute > 1 process at the same time.
    
    ---
    
    ### Advantages
    
    - **Increases** **throughput**
    - If one processor **fails**, another can take charge
    
    ### Disadvantages
    
    - More **complex** **& difficult** to understand
    
    ---
    
    ### Real-Time Operating System
    
    - Carries a certain deadline within which the job is to be completed
        - [ If not done, even if result is produced, loss will be huge ]
    - **Application**
        - Military applications ( missile dropped with absolute precision )
    - **Types**
        - **Hard Real-Time OS**
            - Time constraints are very strict
            - Built for saving life
            - Virtual memory isn’t found
        - **Soft Real-Time OS**
            - Time constraint isn’t very strict
    
    ---
    
    ### Distributed Operating System
    
    <aside>
    ❓ Not installed on single machine
    It is divided into parts located on different machine
    
    </aside>
    
    - More complex, large & sophisticated
        - Because they have to take care of varying network protocols
    
    ### Advantages
    
    - **Failure** of one won’t affect another ( all systems are independent )
    - Email increases **data exchange speed**
    - **Computation is fast & durable** because resources are shared
    - **Load** on host computer **reduces**
    - Easily **scalable**
    - Reduced delay in data processing
    
    ### Disadvantages
    
    ---
    
    ### Network Operating System
    
    ### Advantages
    
    - **Stable** centralised servers
    - **Security concerns** handled by servers
    - **New tech** & hardware is easily integrated
    - **Remote server access**
    
    ### Disadvantages
    
    - **Costly** Servers
    - Depends upon **central location for most operations**
    - Regular **maintenance & updates** are required regularly.
    
    ---
    
    # Structure of Operating System
    
    Depends mainly on how various common components of the operating system are interconnected & moulded into the kernel
    
    - Types
        - Simple
        - Monolithic
        - Hybrid-Kernel
        - Exo-Kernel
        - Layered
        - Modular
        - Virutal
    
    ---
    
    ### Simple Structure
    
    eg : MS-DOS
    
    - No well defined structures
    - Small, simple & limited systems
    - Interface & level of functionality isn’t well separated
    - Can access basic I/O services
    - Causes entire system to crash if one user program fails
    
    ### Advantages
    
    - Better **application performance**
        - Because only few interfaces b/w application program & hardware
    - Easy for **Kernel devs** to develop this OS
    
    ### Disadvantages
    
    - Very **complicated**
        - No clear **boundaries b/w modules**
    - Doesn’t enforce data hiding in OS
    
    ---
    
    ### Monolithic Structure
    
    eg : Linux
    
    - OS Kernel is designed to provide OS Services
        - Memory Management
        - Process Sheduling
        - Device Drivers
        - File Systems
    - All code runs in Kernel Space
        - No separation b/w kernel & user-level processes
    
    ### Advantages
    
    Provide high performance
    
    - Since system calls can be made directly to kerna=el
    - Simpler design
        - Since OS systems are provided by a single binary
    
    ### Disadvantages
    
    - Less secure & stable
        - Since code runs in kernel, all bugs can affect entire system
    
    ---
    
    ### Layered Structure
    
    eg : Linux
    
    - OS can be broken into layers ( levels ) & retain much more control on the system
    - Layer 0 : Hardware  ;  Layer N : User-Interface Layer
    - Each layer uses functions of lower layers only
    - Simplifies debugging
        - Error must be on lower layers
    
    ### Advantages
    
    - Layering makes it easier to enhance OS
        - as implementation of layer can be changed w/o affecting others
    - Very easy to perform debugging & system verification
    
    ### Disadvantages
    
    - Application performance is degraded as compared to simpler structures
    - Requires careful planning for designing laters
        - as each layer can only use functionalities of lower levels
    
    ---
    
    ### Micro-Kernel Structure
    
    - OS broken into pieces
        - and removes all non-essential components from the kernel
    
    ---
    
    ### Modular Structure
    
    - Considered as best approach for an OS
    - Involves designing on modular kernel
    
    ---
    
    ### Hybrid-Kernel Structure
    
    - Combination of monolithic & micro-kernel structures
    
    # Services of OS
    
    - Program Execution
    
    ---
    
    - File Management
    
    ---
    
    - Resource Mangement
    
    ---
    
    - Error Handling
    
    ---
    
    - I/O Operations
    
    ---
    
    - Process Management
    
    ---
    
    - User Interface
    
    ---
    
    - Time Management
    
    ---
    
    - Communication b/w Processes
    
    ---
    
    - Security & Privacy
    
    ---
    
    - Networking
    
    ---