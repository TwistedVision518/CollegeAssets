# {OS} 2. Processes & Process Management

Course: Operating Systems
Confidence: Not Confident
Last Edited: September 9, 2024 11:11 PM

- August 5, 2024
    
    # Introduction
    
    - A process is the unit of work in modern time-sharing systems.
    - A system has a collection of processes - user & system processes .
    - All these processes can execute concurrently with CPU multiplexed among them.
    - A process is a ***program in execution ( running program ).***
    - The execution of a process progresses in a sequential fashion.
    - A program is a passive entity while a process in an active entity.
    - A process includes more than just the program code
    
    ---
    
    - A process is defined as an entity which represents the basic unit of work to be implemented in the system.
    - An instance of running program. The entity that can be assigned to process set execution the operation.
    - A computer program becomes a process which is in main memory ( RAM ).
    - To put in simple words:
        - we write computer programs in a text file & when we execute this program, it becomes a process which performs all the tasks mentioned in the program
        - When program is loaded into memory, it becomes a process,
        - Can be divided into - ***STACK, HEAP, TEXT & DATA***.
    
    <aside>
    ❓ Stack : Contains the temp data such as method/function parameters, return address 
                    & local variables. Used during function call in a program
    
    </aside>
    
    <aside>
    ❓ Heap : Dynamically allocated memory to a process during its runtime
    
    </aside>
    
    <aside>
    ❓ Text : Includes the current activity represented
    
    </aside>
    
    <aside>
    ❓ Data : Region of memory that stores global and static variables that are explicitly 
                   initialized by the programmer.
    
    </aside>
    
    ---
    
    ## Process Control Block (  PCB )
    
    - Data structure maintained by OS for every process.
    - Identified by an integer process ID ( PID ).
    - Keeps all info needed to keep track of a process a.k.a ***task control block***
    
    ==================================================================
    
    - PID
        - UID for each process in OS
    - Process State ( at least 5 states )
        - Current state of the process
    - Process Privileges
        - Required to allow/disallow access to system resources
    - Pointer
        - Pointer to parent process
    - Program Counter
        - Pointer to the address of the next instruction to be executed for this process
    - CPU Registers
        - Where process needs to be stored for execution at running state
    - CPU Scheduling Information
        - Process priority & other scheduling info which is required to schedule the process
    - Memory Management Information
        - Includes info of page table, memory limits, segment table depending on memory used by OS
    - Accounting Information
        - Includes the amount of CPU used for process execution, time limits, execution ID
    - I/O Status Information
        - Includes a list of I/O devices
    
    ---
    
    ### Process States
    
    ![IMG_8167.heic](IMG_8167.heic)
    
    <aside>
    ❓ Long  Term Scheduler
    Short Term Scheduler
    ————————————
    
    </aside>
    
    - New/Start
        - Process is being created
    - Ready
        - Process is waiting to be assigned to a processor
        - Ready processes are waiting to have the processor allocated to them by the OS so that they can run.
        - Process may come into this state after ***START*** state or while running by but interrupted by the scheduler to assign CPU to some other process
    - Running
        - Once the process has been assigned to a processor by the OS Scheduler, the process state us set to running & the process executes its instructions
    - Waiting
        - The process is waiting for some event to occur.
        - ( Such as an I/O completion or reception of a signal ).
    - Terminated/Exit
        - Once the process finishes its execution, or is terminated by the OS, it is moved to the terminated state where it waits to be removed from the main memory
    
    ![IMG_8168.HEIC](2cbaa657-9f4c-4ca9-b626-225a2d7955c9.png)
    
    - Suspend Ready
        - Process that was initially in ready state but was swapped out of main memory & placed onto external storage by the scheduler is said to be in suspended ready state.
        - The process will transition back to a ready state when the process is again brought onto the main memory
    - Suspend Wait or Suspend Blocked
        - Similar to suspend ready
        - Uses the process which was performed by I/O operation & lack of main memory caused them to move to secondary memory. When work is finished, it may go to suspend ready
    - CPU & I/O Bound Process
        - If the process is intensive in terms of CPU operations, then it called CPU Bound Process .
        - If the process is intensive in terms of I/O operations, then it is called I/O Bound Process
    
    ---
    
    ## CPU Scheduler
    
    ### Long Term Scheduler
    
    - Decides how many processes should stay in ready state.
        - i.e. Decides the degree of multiprogramming.
    - Runs infrequently ( hence the name *“Long-Term”* )
    
    ### Short Term Scheduler ( CPU Scheduler )
    
    - Decides which process should be executed next & call for *“dispatcher”*
    - In other words - **Context Switching**
    - Runs frequently
    
    ### Medium Scheduler
    
    - Suspension decision.
    - Used for *swapping* - Moving process from main  to secondary memory & vice-versa
        - Done to reduce the degree of programming
    
    ---
    
    ## Context Switch
    
    - Mechanism to store & restore the state/context of a CPU in PCB so that a process execution can be resumed from the same point a at later time.
    - Enables multiple processes to share a single CPU.
    - Working
        
        When scheduler switches CPU from executing one process to execute another, the state from the current running process is stored into the PCB.
        
        After this, state for the process to run next is loaded from its own PCB & used to set PC, registers etc. At this point, second process can start executing.
        
    - Computationally intensive since register & memory state must be saved & restored.
    To avoid amount of context switching, some hardware systems employ 2/more sets of processor registers
    - Following information is stored for later use
    
    Program Counter
    
    Currently Used Register
    
    Accounting Information
    
    Scheduling Info
    
    Changed State
    
    Base & Limit Register Value
    
    I/O State Information
    
    ---
    
    ## Process Scheduling
    
    - Activity of the process manager that handles the removal of running process from CPU & selection of another process on the basis of a particular strategy.
    - Allows more than one process to be loaded into executable memory at a time & the loaded process shares the CPU using ***‘Time Multiplexing’***
    
    ### Scheduling Criteria
    
    - **CPU Utilisation**
        - Main objective of any CPU scheduling algorithm is to keep the CPU as busy as possible
    - **Throughput**
        - Measure of work done by CPU
        - Number of processes being executed & completed per unit time.
    - **Turnaround Time**
        - How long does it take to execute that process
        - Time taken from submission of process to the time of completion
        - Includes time spent waiting in ready queue, executing in CPU & waiting for I/O
    - **Waiting Time**
        - Time spent by process waiting in ready queue
    - **Response Time**
        - In an interactive system, turn-around time isn’t the best criteria.
        - A process may produce some output early & continue computing new results while previous results are being output to the user
        - Response Time:
            - Time taken from submission of process of request until the first response is produced
    
    ---
    
    ## Scheduling Algorithms
    
    - Process of determining which process will own CPU for execution while another process is on hold.
    - Main task : To make sure that whenever the CPU remains idle, the OS selects at least one of the processes available in the ready state
    
    - Types
        1. Preemptive:
            - Tasks assigned with their priorities
        2. Non-Preemptive:
            - CPU has been allocated to a specific process
            - Will keep the CPU busy until switching context or terminating.

---

- August 7, 2024
    
    ## When scheduling is Preemptive or Non-preemptive?
    
    ![Untitled-2024-08-07-1051-2.png](Operating%20Systems/Assets/Untitled-2024-08-07-1051-2.png)
    
    4 parameters
    
    1. A process switches from running to the waiting state. ***( NP )***
    2. Specific process switches from the running state to the ready state. ***( P )***
    3. Specific process switches from waiting state to ready state. ***( P )***
    4. Process finished its execution & terminated. ***( NP )***
    
    ### Terminologies
    
    - Burst Time / Execution Time / Running Time ( Duration )
        - Time required by the process to complete execution.
    - Arrival Time
        - When a process enters to a ready state
    - Finish Time
        - When a process completes & exits from the system
    - Turnaround Time
        - Completion time - Arrival Time
    - Waiting Time
        - Turn Around Time - Burst Time
    - Multiprogramming
        - No: of programs which can be presented in memory at the same time
    - Jobs
        - Type of program which can be present in memory at the same time
    - User
        - Kind of program having user interaction
    - Process
        - Reference that is used for job & user
    - CPU / IO Burst Cycle
        - Characterises process execution, which alternates b/w CPU & I/O activity.
        - CPU times are usually shorter than the time of I/O
    
    <aside>
    ❓ Multiprogramming   :   Preemptive
    Multiprocessing          :   Non Preemptive 
    Multitasking                 :   Preemptive
    
    Preemptive            : Allows process to be interrupted by high-priority process
    Non-preemptive : Any new  process should wait until the running process finishes its  
                                            CPU cycle.
    
    </aside>
    
    ## Scheduling Algorithms ( 6 Types )
    
    - First Come First Serve ***( FCFS )***
    - Shortest Job First ***( SJF )***
    - Shortest Remaining Time First
    - Priority Scheduling
    - Round Robin Scheduling
    - Multilevel Queue Scheduling
    
    <aside>
    💡 algor
    
    </aside>
    
    ## First Come First Serve ( Arrival Time ) ( NP )
    
    | Process ID | Arrival Time | Burst Time | Completion Time
    ( Prev CT + Curr BT ) | Turnaround Time 
    ( CT - AT ) | Waiting Time
    ( TAT - BT ) |
    | --- | --- | --- | --- | --- | --- |
    | P1 | 0 | 3 | 3 | 3 | 0 |
    | P2 | 1 | 4 | 7  | 6 | 2 |
    | P3 | 2 | 2 | 9 | 7 | 5 |
    | P4 | 3 | 1 | 10 | 7 | 6 |
    
    | Process ID | Arrival Time | Burst Time | Completion Time
    ( Prev CT + Curr BT ) | Turnaround Time 
    ( CT - AT ) | Waiting Time
    ( TAT - BT ) |
    | --- | --- | --- | --- | --- | --- |
    | P1 | 0 | 2 | 2 | 2 | 0 |
    | P2 | 1 | 2 | 4 | 3 | 1 |
    | P3 | 5 | 3 | 8 | ADDING IDLE | 3 | 0 |
    | P4 | 6 | 4 | 12 | 6 | 2 |
    - Since after P2, CPU is idle for 1 unit of time
    
    <aside>
    ❓ Check Out Gantt Chart
    
    </aside>
    
    ## Shortest Job First ( Burst Time ) ( NP )
    
    | Process | Arrival Time | Burst Time | Completion Time
    ( Prev CT + Curr BT ) | Turnaround Time 
    ( CT - AT ) | Waiting Time
    ( TAT - BT ) |
    | --- | --- | --- | --- | --- | --- |
    | P1 | 1 | 3 | 6 | 5 | 2 |
    | P2 | 2 | 4 | 10 | 8 | 4 |
    | P3 | 1 | 2 | 3 | 2 | 0 |
    | P4 | 4 | 4 | 14 | 10 | 6 |
    
    ## Shortest Time Remaining ( Burst Time ) ( P )
    
    | Process ID | Arrival Time | Burst Time | Completion Time
    ( Prev CT + Curr BT ) | Turnaround Time 
    ( CT - AT ) | Waiting Time
    ( TAT - BT ) |
    | --- | --- | --- | --- | --- | --- |
    | P1 | 0 | 5 | 8 | 8 | 3 |
    | P2 | 1 | 3 | 4 | 3 | 0 |
    | P3 | 2 | 4 | 12 | 10 | 6 |
    | P4 | 4 | 10 | 22 | 18 | 8 |

---

- August 8, 2024
    
    ## Round Robin ( Time Quantum ) ( P )
    
    Time Quantum = 2 ***( THIS ANSWER IS WRONG )***
    
    | Process ID | Arrival Time | Burst Time | Completion Time
    ( Prev CT + Curr BT ) | Turnaround Time 
    ( CT - AT ) | Waiting Time
    ( TAT - BT ) | RS
    Process - AT |
    | --- | --- | --- | --- | --- | --- | --- |
    | P1 | 0 | ~~5~~ ~~3~~ ~~1~~ | 12 | 12 | 7 | 0 |
    | P2 | 1 | ~~4~~ ~~2~~  | 11 | 10 | 6 | 1 |
    | P3 | 2 | ~~2~~ | 6 | 4 | 2 | 2 |
    | P4 | 4 | ~~1~~ | 9 | 5 | 4 | 4 |
    
    ![Untitled](Operating%20Systems/Assets/Untitled.png)
    
    ---
    
    Time Quantum = 5
    
    | Process ID | Arrival Time | Burst Time | Completion Time
    ( Prev CT + Curr BT ) | Turnaround Time 
    ( CT - AT ) | Waiting Time
    ( TAT - BT ) | Response Time
    Process - AT |
    | --- | --- | --- | --- | --- | --- | --- |
    | P1 | 0 | ~~7~~ ~~2~~ | 31 | 31 | 24 | 0 |
    | P2 | 1 | ~~4~~ | 9 | 8 | 4 | 4 |
    | P3 | 2 | ~~15~~ ~~10~~ ~~5~~ | 55 | 53 | 38 | 7 |
    | P4 | 3 | ~~11~~ ~~6~~ ~~1~~ | 56 | 53 | 42 | 11 |
    | P5 | 4 | ~~20~~ ~~15~~ ~~10~~ | 66 | 62 | 42 | 15 |
    | P6 | 4 | ~~9~~ ~~4~~ | 50 | 46 | 37 | 20 |
    
    ![Untitled](Operating%20Systems/Assets/Untitled%201.png)
    

---

- August 14, 2024
    
    ## Priority Scheduling Algorithm ( Highest Priority ) ( P )
    
    - 1.
        
        
        | Priority | Process ID | AT | BT | CT | TAT | WT | RT |
        | --- | --- | --- | --- | --- | --- | --- | --- |
        | 2 ( L ) | P1 | 0 | ~~4~~ ~~3~~ | 15 | 15 | 11 | 0 |
        | 3 | P2 | 1 | ~~3~~ ~~2~~ | 12 | 11 | 8 | 0 |
        | 4 | P3 | 2 | ~~1~~ | 3 | 1 | 0 | 0 |
        | 5 ( H ) | P4 | 3 | ~~5~~ | 8 | 5 | 0 | 0 |
        | 5 ( H ) | P5 | 4 | ~~2~~ | 10 | 6 | 4 | 4 |
        
        ![image.png](Operating%20Systems/Assets/image.png)
        
    - 2.
        
        
        | Priority | Process ID | Arrival Time | Burst Time | Completion Time
        ( Prev CT + Curr BT ) | Turnaround Time 
        ( CT - AT ) | Waiting Time
        ( TAT - BT ) |
        | --- | --- | --- | --- | --- | --- | --- |
        | 2 | P1 | 0 | ~~10~~ ~~8~~ | 17 | 17 | 7 |
        | 1 | P2 | 2 | ~~5~~ ~~4~~ | 9 | 7 | 2 |
        | 0 ( H ) | P3 | 3 | ~~2~~ | 5 | 2 | 0 |
        | 3 ( L ) | P4 | 5 | ~~20~~ | 37 | 32 | 12 |
        
        ![image.png](Operating%20Systems/Assets/image%201.png)
        
    
    ## Priority Scheduling Algorithm ( Highest Priority ) ( NP )
    
    - 1.
        
        
        | Priority | Process ID | AT | BT | CT | TAT | WT | RT |
        | --- | --- | --- | --- | --- | --- | --- | --- |
        | 2 ( L ) | P1 | 0 | 4 | 4 | 4 | 0 | 0 |
        | 3 | P2 | 1 | 3 | 15 | 14 | 11 | 11 |
        | 4 | P3 | 2 | 1 | 12 | 10 | 9 | 9 |
        | 5 ( H ) | P4 | 3 | 5 | 9 | 6 | 1 | 1 |
        | 5 ( H ) | P5 | 4 | 2 | 11 | 7 | 5 | 5 |
        
        ![image.png](image%202.png)
        
    - 2.
        
        
        | Priority | Process ID | Arrival Time | Burst Time | Completion Time
        ( Prev CT + Curr BT ) | Turnaround Time 
        ( CT - AT ) | Waiting Time
        ( TAT - BT ) |
        | --- | --- | --- | --- | --- | --- | --- |
        | 2 | P1 | 0 | 10 | 10 | 10 | 0 |
        | 1 | P2 | 2 | 5 | 17 | 15 | 10 |
        | 0 ( H ) | P3 | 3 | 2 | 12 | 9 | 7 |
        | 3 ( L ) | P4 | 5 | 20 | 37 | 32 | 12 |
        
        ![image.png](image%203.png)
        

---

- August 21, 2024
    
    
    | Priority | Process ID | AT | BT | CT | TAT | WT | RT |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 5 ( L ) | P1 | 3 | 1 |  |  |  |  |
    | 5 ( L ) | P2 | 1 | 4 |  |  |  |  |
    | 4 | P3 | 4 | 2 |  |  |  |  |
    | 1 ( H ) | P4 | 0 | 6 |  |  |  |  |
    | 2  | P5 | 2 | 3 |  |  |  |  |
    
    ## First Come First Serve
    
    | Priority | Process ID | AT | BT | CT | TAT | WT | RT |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 5 ( L ) | P1 | 3 | 1 | 14 | 11 | 10 | 10 |
    | 5 ( L ) | P2 | 1 | 4 | 10 | 9 | 5 | 5 |
    | 4 | P3 | 4 | 2 | 16 | 12 | 10 | 10 |
    | 1 ( H ) | P4 | 0 | 6 | 6 | 6 | 0 | 0 |
    | 2  | P5 | 2 | 3 | 13 | 11 | 8 | 8 |
    
    ![image.png](image%204.png)
    
    **Average TurnAround Time =   $(11 + 9 + 12 + 6 + 11 ) / 5 = 9.8$**
    
    **Average Waiting Time =   $( 10 + 5 + 10 + 0 + 8 ) / 5 = 6.6$**
    
    ## Shortest Job First
    
    | Priority | Process ID | AT | BT | CT | TAT | WT | RT |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 5 ( L ) | P1 | 3 | 1 | 7 | 4 | 3 | 3 |
    | 5 ( L ) | P2 | 1 | 4 | 16 | 15 | 11 | 11 |
    | 4 | P3 | 4 | 2 | 9 | 5 | 3 | 3 |
    | 1 ( H ) | P4 | 0 | 6 | 6 | 6 | 0 | 0 |
    | 2  | P5 | 2 | 3 | 12 | 10 | 7 | 7 |
    
    ![image.png](Operating%20Systems/Assets/image%205.png)
    
    **Average TurnAround Time =   $( 4 + 15 + 5 + 6 + 10 ) / 5 = 8$**
    
    **Average Waiting Time =   $( 3 + 11 + 3 + 0 + 7 ) / 5 = 4.8$**
    
    ## Shortest Remaining Time First
    
    | Priority | Process ID | AT | BT | CT | TAT | WT | RT |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 5 ( L ) | P1 | 3 | ~~1~~ | 4 | 1 | 0 | 0 |
    | 5 ( L ) | P2 | 1 | ~~4~~ ~~2~~ | 6 | 5 | 1 | 0 |
    | 4 | P3 | 4 | ~~2~~ | 8 | 4 | 2 | 2 |
    | 1 ( H ) | P4 | 0 | ~~6~~ ~~5~~ | 16 | 16 | 10 | 0 |
    | 2  | P5 | 2 | ~~3~~ | 11 | 9 | 6 | 6 |
    
    ![image.png](Operating%20Systems/Assets/image%206.png)
    
    **Average TurnAround Time =   $( 1 + 5 + 4 + 16 + 9 ) / 5 = 7$**
    
    **Average Waiting Time =   $( 0 + 1 + 2 + 10 + 6 ) / 5 = 3.8$**
    
    ## Round Robin ( Time Quantum = 3 )
    
    | Priority | Process ID | AT | BT | CT | TAT | WT | RT |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 5 ( L ) | P1 | 3 | ~~1~~ | 10 | 7 | 6 | 6 |
    | 5 ( L ) | P2 | 1 | ~~4~~ ~~1~~ | 16 | 15 | 11 | 2 |
    | 4 | P3 | 4 | ~~2~~ | 15 | 11 | 9 | 9 |
    | 1 ( H ) | P4 | 0 | ~~6~~ ~~3~~ | 13 | 13 | 7 | 0 |
    | 2  | P5 | 2 | ~~3~~ | 9 | 7 | 4 | 4 |
    
    ![image.png](Operating%20Systems/Assets/image%207.png)
    
    **Average TurnAround Time =   $( 7 + 15 + 11 + 13 + 7 ) / 5 = 10.6$**
    
    **Average Waiting Time =   $( 6 + 11 + 9 + 7 + 4 ) / 5 = 7.4$**
    
    ## Priority ( Preemptive )
    
    | Priority | Process ID | AT | BT | CT | TAT | WT | RT |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 5 ( L ) | P1 | 3 | 1 | 16 | 13 | 12 | 12 |
    | 5 ( L ) | P2 | 1 | 4 | 15 | 14 | 10 | 10 |
    | 4 | P3 | 4 | 2 | 11 | 7 | 5 | 5 |
    | 1 ( H ) | P4 | 0 | 6 | 6 | 6 | 0 | 0 |
    | 2  | P5 | 2 | 3 | 9 | 7 | 4 | 4 |
    
    ![image.png](Operating%20Systems/Assets/image%208.png)
    
    **Average TurnAround Time =   $( 13 + 14 + 7 + 6 + 7 ) / 5 = 9.4$**
    
    **Average Waiting Time =   $( 12 + 10 + 5 + 0 + 4 ) / 5 = 6.2$**
    
    ## Priority ( Non - Preemptive )
    
    | Priority | Process ID | AT | BT | CT | TAT | WT | RT |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 5 ( L ) | P1 | 3 | 1 | 16 | 13 | 12 | 12 |
    | 5 ( L ) | P2 | 1 | 4 | 15 | 14 | 10 | 10 |
    | 4 | P3 | 4 | 2 | 11 | 7 | 5 | 5 |
    | 1 ( H ) | P4 | 0 | 6 | 6 | 6 | 0 | 0 |
    | 2 | P5 | 2 | 3 | 9 | 7 | 4 | 4 |
    
    ![image.png](Operating%20Systems/Assets/image%208.png)
    
    **Average TurnAround Time =   $( 13 + 14 + 7 + 6 + 7 ) / 5 = 9.4$**
    
    **Average Waiting Time =   $( 12 + 10 + 5 + 0 + 4 ) / 5 = 6.2$**
    

---

- August 28, 2024
    
    ## Multiple Level Queues Scheduling
    
    - Not independent scheduling algorithm. They make use of other existing algorithms to group & schedule jobs with common characteristics.
    - Multiple queues are maintained for processes with common characteristics.
    - Each queue can have its own scheduling algorithms.
    - Priorities are assigned to each queue.
    - eg;
        - CPU-bound jobs can be scheduled in one queue & I/O-bound processes can be bound in another queue.
        - Process scheduler than alternately select jobs from each queue & assigns them to CPU based on algorithm assigned to the queue.
        - Processes could be high-priority, foreground ( interactive ) process & background         ( batch ) processes.
    
    ```mermaid
    graph TD
    subgraph Multiple-Level Queues Scheduling
    	HP(High Priority) ---> LP(Low Priority)
    	SP(System Processes) --> IP(Interactive Processes)
    	IP --> BP(Batch Processes)
    	
    	Queue1 --> Queue2 --> Queue3
    end
    
    ```
    
    ---
    
    Question
    
    RR ( TQ = 2 ) ; FCFS 
    
    | Queue No: | Process ID | AT | BT | CT | TAT | WT | RT |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 1 | P1 | 0 | 5 |  |  |  |  |
    | 1 | P2 | 0 | 3 |  |  |  |  |
    | 2 | P3 | 0 | 8 |  |  |  |  |
    | 1 | P4 | 10 | 5 |  |  |  |  |
    
    ![image.png](Operating%20Systems/Assets/image%209.png)
    
    ---
    
    ## OS Services For Process & Thread Management
    
    ### Threads
    
    - It is the flow of execution through the process code, w/ its own program counter that keeps track of which instruction to execute next, system registers which hold its current working variables & a stack which contains the execution history. It comprises of
        - Thread ID
        - Program Counter
        - Register Set
        - Stack
    - Thread shares with its peer threads few information like
        - Code Segment
        - Data Segment
        - Open Files
    - When one thread alters a code segment memory item, all other threads see that
    - a.k.a ***LightWeight Process** :*
        - Provides a way to improve application performance ( parallelism )
    - 000
    - Each thread belongs to one process. No thread can exist out of a process
    - 000
    - 000
    
    <aside>
    💡 Types of Threads :  ***User Level & Kernel Level***
    
    </aside>
    
    ![image.png](image%2010.png)
    
    ```mermaid
    graph TD
    
    subgraph Single Process with Three Threads
    	subgraph 4
    	 R1(Register) -.- C1(Counter) -.- S1(Stack)
    	 R2(Register) -.- C2(Counter) -.- S2(Stack)
    	 R3(Register) -.- C3(Counter) -.- S3(Stack)
    	end
    	subgraph 5
    		Data
    		Files
    	end
    	subgraph 6
    		Code -.- T1(First Thread)
    		Code -.- T2(First Thread)
    		Code -.- T3(First Thread)
    		
    	end
    	
    	4 -.- 5 -.- 6
    end
    
    subgraph Single Process with Single Thread
    	subgraph 1
    		Re(Register)
    		Co(Counter)
    		St(Stack)
    	end
    	subgraph 2
    		Da(Data) 
    		Fi(Files)
    	end
    	subgraph 3
    		C(Code) -..- ST(Single Thread)
    	end
    	1 -.- 2 -.- 3
    end
    ```
    
    ---