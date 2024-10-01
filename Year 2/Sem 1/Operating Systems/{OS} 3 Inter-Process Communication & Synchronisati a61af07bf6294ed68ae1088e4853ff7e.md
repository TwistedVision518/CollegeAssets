****# {OS} 3. Inter-Process Communication & Synchronisation Deadlocks

Course: Operating Systems 
Confidence: Not Confident


- Roadmap
    - Intro To Message Passing
        - Race Condition
        - Critical Section Problem
        - Mutual Exclusion w/ busy waiting - disabling interrupts
    - Lock Variables
    - Peterson’s Solution
    - TSL Instructions
    - Busy Waiting
    - Sleep & Wake Up Calls
    - Semaphore
    - Monitors
    - Classical Epic Problems
    - Deadlock - System Model
    - Resource Types
    - 
    
    - Deadlock Problem
    
    - Analysis for Deadlock Handling
    
    - Deadlock Prevntion
    
    - Deadlock Avoidance
    - Deadlock Detection
    - Recovery From Deadlock

---

- August 28, 2024
    
    ## Introduction
    
    Inter-process communication is the mechanism provided by the OS that allows processes to communicate with each other.
    
    Could involve a process letting another one know that some event has occurred or transferring of data from one process to another.
    
    <aside>
    💡 Inter-process communication is used for **exchanging useful info b/w numbers threads in 1/more processes/programs.**
    
    </aside>
    
    ```mermaid
    graph LR
      P1(Process P1) <--> |Interprocess Communication| P2(Process P2)
    ```
    
    1. Dependent Processes
        1. Shared Memory
        2. Message Passing
    - Todo
        1. Write a note on MultiLevel Queue Scheduling w/o using ChatGPT
        2. Explain the concept of threads with multithreading

---

- September 2, 2024
    
    ### Process Synchronisation
    
    Introduced to handle problems that arose while multiple process executions.
    
    1. Independent Process
    2. Dependent / Cooperative Process
    
    ### Methods of IPC
    
                        **Shared Memory**
    
    ![Untitled-2024-08-07-1051-5.png](Operating%20Systems/Assets/Untitled-2024-08-07-1051-5.png)
    
    The two processes share a common memory location known as a **buffer**.
    
                        **Message Parsing**
    
    ![Untitled-2024-08-07-1051-6.jpeg](Operating%20Systems/Assets/Untitled-2024-08-07-1051-6.jpeg)
    
    Processes communicate with each other without using any kind of shared memory.
    
    ---
    
    ## Process Synchronisation
    
    - Task phenomenon of coordinating the execution of processes in such a way that no tow processes can have access to the same shared data & resources.
    - In order to preserve the appropriate order of execution of cooperative processes.
    - Mainly needed in multi-process system when multiple processes are running together & more than one processes try to gain access to same shared resource or any data at the same time.
    
    ---
    
    ## Critical Section Problem
    
    An atomic action is required in a critical section ( i.e. only one process can execute in its critical section at a time ). All other processes have to wait to execute in their critical sections
    
    ```cpp
    do {
    	//entry section
    			//critical section
    	//exit section
    			//remainder section
    } while(true)
    ```
    
    **Entry Section :** 
    
    Acquires resources needed for process execution 
    
    **Exit Section :**
    
    Handles exit from the critical section. Releases resources & informs other processes that critical section is free
    
    ---
    
    ## Race Condition
    
    At the time when more than one process is either executing the same code or accessing the same memory or any shared variable, there is a possibility that the output or the value of shared variable is wrong. For this purpose all processes are racing to say that their output is correct.
    
    - Since several processes access & process the manipulations on the same data in a concurrent manner,
        - the outcome depends in the ***particular order*** in which the access of data takes place.
    - Mainly this condition is a situation that may occur inside the critical section.
        - Race condition in the critical section happens when the result of multiple thread executions differs according to the order in which the threads execute.
        - But this condition is critical sections can be avoided if the critical section is treated as an atomic instruction.
        - Proper thread synchronisation using locks or atomic variables can help avoid this
    
    ---
    
    ## Solution to Critical Section Problem
    
    1.                                                                             **Mutual Exclusion**
    It implies that only one process can be inside the critical section at any time. If any other processes require the critical section, they must wait until its free.
    
    ---
    
    1.                           **Progress**
    If a process is not using the critical section, then it should not stop any other process from accessing it.
        
        ---
        
    
    ---
    
    1.                  **Bounded Waiting**
    Each process must have a limited waiting time. It should not wait endlessly to access the critical section
        
        ---
        

---

- September 4, 2024
    
    > **Peterson Solution/tu**
    > 
    > 
    > Whenever a process is executing in any critical state, the other process executes the rest of the code & vice-versa. This method also helps to make sure that only a single process can run in the critical section at a specific time. 
    > 
    > > *( Only 2 processes can run parallel with this solution )*
    > > 
    > 
    > It is a **Software Based solution**.
    > 
    > - It preserves the conditions
    >     1. Mutual exclusion is comforted as at any time only one process can access the critical section
    >     2. Progress is also comforted, as a process that is outside the critical section is unable to block other processes from entering into the critical section
    >     3. Bounded Waiting is assured as every process gets a fair chance to enter the Critical Section
    > 
    > - Code
    >
> ### C+
> 
> ```cpp
> //-----------------------------------------------------------
> //entry section (process)
> {
> 	int other;
> 	other = 1-process;
> 	interested[process] = true;
> 	turn = process;
> 	
> 	while(interested[other] == true && turn == process);
> }
> //-----------------------------------------------------------
> //critical section
> //-----------------------------------------------------------
> //exit section
> {
> 		interested[process] = false;
> }
> //-----------------------------------------------------------
> ```
> 
> - Java
> 
> ```java
> { // entry section
> 			var other = 1 - process;
> 			this.interested[process] = true;
> 
> 			this.turn = process;
> 
> 			// infinite loop if the other process is running
> 			while (interested[other] && this.turn == process) {
> 				System.out.printf("%d in waiting%n", process);
> 			}
> 		}
> 
> 		{ // Critical Section
> 			System.out.printf("Process-[%d] enters the critical section%n", process);
> 
> 				Thread.sleep(1);
> 		}
> 
> 		{ // exit section
> 			this.interested[process] = false;
> 		}
> }
> ```
> 
> 
> ---
    > 
    > - 2 shared variables :
    >     - boolean flag[i] :   Init `false`
    >     - int turn                :