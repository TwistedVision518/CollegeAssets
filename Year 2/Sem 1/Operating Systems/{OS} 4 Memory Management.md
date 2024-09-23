# {OS} Synchronization Mechanisms

Course: Operating Systems (Operating%20Systems%20f7a5c52a1398467487fc5042b3a10069.md)
Confidence: Not Confident
Last Edited: September 11, 2024 10:50 AM

Synchronization is the process of preventing two processes from executing the critical section simultaneously.

### Busy waiting and sleep waiting (without busy waiting)

**Busy waiting** is defined as a process synchronization technique where the process waits and continuously keeps on checking for the condition to be satisfied before going ahead with its execution.

This method is also not viable since it *wastes CPU resource*. This is because other process are close to critical section, in an infinite loop thus wasting CPU resource.
Also *Busy waiting* does not consider the priority of the processes.

Due to this disadvantage of busy waiting, *sleep waiting* is used.

---
**Sleep waiting** simply says that if the process is waiting for the lock on critical section, process goes to sleep until the lock is lifted.

The process which is executing the critical section notifies the sleeping process when its done executing the critical section. In some cases, the OS may also notify the sleeping processes.

---

#### Sleep and wake up calls

##### Semaphores:
- `wait`, `sleep` and `down` (`P`)
- `signal`, `wake-up` and `up` (`V`)

---

```c
  #define BufferSize 100;
  int count = 0;

  Producer()
  {
    int item;
    WHILE (true) {                   // loop forever
      item = produce_item();              // create a new widget to put in the buffer
      if(count==BufferSize)
           Sleep();                  // if the buffer is full, sleep
      insert_item(item);              // put the item in the buffer
      count = count + 1;             // increment count of items
      IF (count>=1)
         Wakeup(Consumer);           // if the buffer was previously empty, wake
   }                                 //  the consumer
  }

  Consumer()
  {
    int item;
    while(true) {                    // loop forever
      IF(count==0)
           Sleep();                  // if the buffer is empty, sleep
      item = remove_item();           // take an item from the buffer
      count = count - 1;             // decrement count of items
      IF(count<=N-1)
            Wakeup(Producer);        // if buffer was previously full, wake
                                     //  the producer
      Consume_item(widget);          // consume the item
     }
   }
```

## Semaphores

Semaphores are just normal variables used to coordinate the activites of multiple processes in a computer system. They are used to enforce mutual exclusion, avoid race conditions, and implement synchronization between processes.

It is used to solve the critical section problem.

It is to be noted that semaphores are shared variables.

`P` and `V` are semaphores helper functions. `S` is a semaphore variable.

```js
P(Semaphore S) {
	while(S == 0){}
	S = S - 1;
}

V(Sempahore S) {
	S = S + 1;
}
````


### Monitors

In an program, we have a set of shared variables.

using **Monitors** is similar to critical section, where only one process can enter the monitor section.

However, in case of monitors, the process has to go through _procedures_ to access the variables. On the other hand, processes can directly access the critical section.

---

#### Classical synchronization problems

### Dining Philosophers problem

There are 5 philosophers sitting on a circular table. There are only 5 forks. Only 2 philosophers can eat at the same time. The solution involves synchronizing philosophers so that everyone can eat their portion equally.

### Reader-Writer problem

There are multiple readers and writers that are trying to access the database to perform some operations. The solution should synchronize in such a way that data integrity and consistency is maintained.

### Sleeping Barber Problem

Initially, the barber is sleeping.

When the first customer arrives, it wakes up the barber. If another customer arrives while the barber is busy, they must wait for the barber to finish. However, if it's taking too much time, then the customer may leave.

Once the barber has finished doing its job, then it will check if there are any customers waiting outside, if there are no customers then the barber will go to sleep until another customer wake him up.

We have to use 3 semaphores in this problem.

---

### Deadlock

Deadlock is a situation in computing where two or more processes are unable to processed because each is waiting for the other to release resources. A condition when 2 or more processes sharing the same resource are effectively preventing each other from accessing the resources known as deadlock.

In case of deadlock, the processes goes into infinite waiting state since the resource it has requested are not available.

```mermaid
graph TD;
R1 --> |allocated|P1
P1 --> |requesting|R2
R2 --> |allocated|P2
P2 --> |requesting|R1
```


There **4 conditions to achieve deadlock**:
1. Mutual exclusion
2. Hold & wait
3. Circular path
4. non-preemption

##### Operations
In normal operation, a process must request a resource before using it and release it when finished, as show below

- Request :- If the request cannot be granted immediately, the process must wait until the resource(s) required to become available. The system, for example, uses the functions open() malloc(), new() and request().
- Use
- Release

##### *Necessary conditions* in order to achieve *deadlock*

1. **Mutual exclusion**:- at least one resource must be kept in a non-shareable state. If another process requests it, it must wait for it to be released.
2. **Hold and wait**:- A process must hold at least one resource while also waiting for at least one resource that another process is currently holding.
3. **No preemption**:- Once a process holds a resource, that resource cannot be taken away from that process until the process voluntarily release it
4. **Circular wait**:- There must be a set of processes $P0, P1, P2,....PN$ such that every $P[i]$ i waiting fro $P[(i + 1)]$ 

Resources can be memory, CPUs, printers, open files, tape drives, CD-ROMs and I/O devices.

There are different types of resources such as:
- Active resource --> CPU, network adapter
- Passive resource --> memory
- Shared resource

### Methods for handling deadlocks
There are mainly four methods for handling deadlocks:-
- **Deadlock prevention**
Prevent one condition out of four from being satisfied, thus preventing the deadlock

- **Deadlock avoidance**
By using multiple resources, we can avoid the deadlock
(?) find more avoidance

- **Deadlock detection & recovery**
We keep checking the four conditions and for every condition that is satisfied, we try to recover from it.

- **Deadlock ignorance** ignored successfully
---

### Memory Management

