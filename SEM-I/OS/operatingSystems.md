<h1 style="color: seagreen;">Booting Process</h1>

- Starts when power button is hit.
- CPU moves to the **BIOS**(Basic Input Output System) in **ROM**(Read Only Memory).
- BIOS will start executing **POST**.
- **Power On Self Test**(POST) 
	- Here all the hardware will be checked/tested and their working condition is informed to the BIOS. When all the hardware is in working condition then only we can load the software into RAM.
	- If any hardware is not working then the Booting process will be stopped.
- When **POST** is successful then BIOS will immediately load **MBR**(Master Boot Record) to **RAM**.
	- MBR is a **512-byte sector**, located in the first sector on the disk.
- After loading MBR the BIOS yields control to it. MBR loads **Boot Loader** to the RAM. 
- Boot Loader loads the operating system from a disk to the RAM and starts executing the operating system.
- **Finally the control will be automatically moved to the Operating system**.

<h2 style="color:khaki">Types of Booting</h2>

- **Hard booting** - Power On the system.
- **Soft booting** - Restart start/ CTRL + ALT + DEL twice

## Boot Loader
software that is responsible for "actually loading" the OS once the Boot Manager has finished its work. 
Loading OS basically means loading the kernel of the OS. Boot loader is typically a part of the OS.
- **GRUB**(Grand Unified Boot Loader) and **LILO** are most popular Linux Boot Loaders. 
	- GRUB - OS independent boot loader.
	- Multiboot software packet from GNU.
	- Flexible command line interface.
	- File system access.
	- Supports diskless system.
	- Download OS from the network.

# Process Management
- A **process** is a program in execution. A process needs certain resources including CPU time, memory, files, and I/O devices to accomplish its task.
- **OS is responsible for the following task in connection with the process management.**
	- Process creation and deletion.
	- Process suspension and resumption.
	- Provision of mechanism for - 1. Process synchronization. 2. Process communication.

## Main Memory Management
- Memory management is a technique that controls and manages the functionality of primary memory. It moves processes from primary memory to secondary memory and vice versa.
- **Main memory**, also known as RAM (Random Access Memory), is the physical memory inside a computer. It's a volatile storage device. It's **where programs and information are stored when the processor is using them**. The computer can only change data in main memory.
- Memory is a large array of words or bytes, each with its won address. It is a repository of quickly accessible data shared by CPU and I/O devices.
- **OS is responsible for the following tasks in connection with the memory management**
	- Keep track of which parts of memory are currently being used and by whom.
	- Decide which processes to load when memory space becomes available.
	- Allocate and deallocate memory space as needed.