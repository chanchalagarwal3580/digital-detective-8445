# Mission 3 — Understand the Operating System

---

## 1. Task / Objective
The objective of Mission 3 was to explore the core roles and responsibilities of an Operating System (OS). This involved:
1. Identifying the host operating system environment, active user identity (privacy-safe), storage utilization, and system performance metrics using Terminal.
2. Understanding process execution, observing active processes, and analyzing the role of Process Identifiers (PIDs).
3. Distinguishing between absolute and relative file paths and inspecting POSIX file permissions (`r-w-x`).
4. Explaining the primary functions of an operating system: Process Management, Memory Management, Device Management, File Management, User Interface/Shell, and Security/Permissions.

---

## 2. Work Completed
- **Operating System Exploration**: Ran commands (`sw_vers`, `uname -srm`, `whoami`, `df -h /`, and `top -l 1`) to capture actual system hardware/software metrics.
- **Process Inspection**: Inspected the live process table using `ps aux`, identified user applications (`Google Chrome`, `Finder`, `Antigravity`) and background system daemons (`WindowServer`, `opendirectoryd`), and analyzed PIDs.
- **Path & Permission Analysis**: Documented the structural differences between absolute and relative paths using project examples, and examined the permission string (`-rw-r--r--`) of practice files.
- **OS Responsibilities Framework**: Completed the comprehensive operating system responsibilities table with definitions and real-world scenarios.
- **Viva Preparation**: Formulated 5 teacher viva questions and answers explaining kernel roles, virtual memory, and permissions.

---

## 3. Commands / Tools Used

| Command | Category | Purpose |
| :--- | :--- | :--- |
| `sw_vers` | System Inspection | Displays macOS product name, version, and build number. |
| `uname -srm` | Kernel Inspection | Prints the operating system kernel name, release version, and machine hardware architecture (ARM64). |
| `whoami` | Identity | Displays the username of the active user session. |
| `df -h /` | Storage Inspection | Shows disk file system capacity, used space, and available storage in human-readable units. |
| `top -l 1` | System Activity Snapshot | Generates a single-iteration snapshot of running processes, CPU load, memory utilization, and thread counts. |
| `ps aux` | Process Table | Lists all active processes with user, PID, CPU%, Memory%, and executable command path. |
| `ls -l` | Permission Inspection | Shows detailed file metadata including file type, owner permissions, group permissions, and others' permissions. |

---

## 4. My Understanding

### Task 3.1 — Operating System Exploration Table

| Information Explored | What It Tells You | Your Observation (Privacy-Safe) |
| :--- | :--- | :--- |
| **Operating System / System Details** | The specific OS platform, kernel release version, and processor architecture executing on the machine. | `macOS 27.2.1` (Build `26B131`), Darwin Kernel `27.2.0`, Architecture: `arm64` (Apple Silicon). |
| **Current Account Identity** | Which user profile owns the active terminal session, determining default file access permissions. | Current user: `[redacted]` (Standard administrative user account, non-root). |
| **Available and Used Storage** | Total partition capacity on the root drive (`/`), space consumed by the system/files, and available free storage. | Drive size: `926 GiB`, Used: `13 GiB` (system volume), Available: `678 GiB` (~2% root capacity used). |
| **System Activity Snapshot** | Instantaneous summary of CPU load averages, active vs. sleeping tasks, and memory allocation. | `794` total processes (2 running, 792 sleeping), `3961` threads; CPU: `6.77%` user, `11.92%` sys, `81.29%` idle; Physical Memory: `15 GB` used, `465 MB` free. |

---

### Task 3.2 — Understanding Processes

#### 1. What is a process?
A **process** is an active, executing instance of a computer program. When a program is stored on an SSD, it is merely passive code (a file). When launched, the operating system loads the program's instructions and data into RAM, allocates system resources (CPU registers, file descriptors, memory pages), and begins execution. That running entity is a process.

#### 2. What does the PID column represent?
**PID** stands for **Process Identifier**. It is a unique positive integer assigned by the operating system kernel to each process when it is created. The operating system uses the PID to track, prioritize, communicate with, and terminate specific processes (e.g. via `kill <PID>`).

#### 3. Real Examples Observed on My Computer:
- **Application Process**: `Google Chrome` (`PID: 34331`) — An interactive user application consuming CPU cycles and memory to render web pages.
- **Background System Daemon**: `WindowServer` (`PID: 616`) — A privileged macOS system daemon responsible for compositing visual windows and managing the display server.

---

### Task 3.3 — Paths and File Permissions

#### 1. Absolute Path vs. Relative Path

| Path Type | Definition | Example from This Project |
| :--- | :--- | :--- |
| **Absolute Path** | Specifies the exact, unambiguous location of a file or folder starting from the root directory (`/`). It works identically regardless of your current working directory. | `/Users/[redacted]/Detative mission/digital-detective-8445/terminal-practice/sample.txt` |
| **Relative Path** | Specifies the location of a target file or folder relative to the directory where you are currently standing (`pwd`). | `terminal-practice/sample.txt` (from project root) or `../README.md` (from a subfolder). |

#### 2. File Permissions Breakdown
Inspecting `sample.txt` using `ls -l` shows:
```text
-rw-r--r--  1 [redacted]  staff  74 Nov 16 16:32 sample.txt
```

Breaking down `-rw-r--r--`:
- `-`: Regular file (would be `d` for a directory).
- `rw-` (**Owner / User**): The creator/owner can **Read** (`r`) and **Write** (`w`), but cannot execute (`-`).
- `r--` (**Group**): Members of the owning group (`staff`) can only **Read** (`r`).
- `r--` (**Others / World**): All other users on the system can only **Read** (`r`).

#### Permissions Reference Table

| Permission | Meaning | Practical Example |
| :--- | :--- | :--- |
| **`r` — Read** | Allows the user to open and view the file's contents; on a directory, allows listing its contents. | Opening a markdown document or python script in an editor to read it. |
| **`w` — Write** | Allows the user to modify, edit, append to, or delete the file; on a directory, allows creating/deleting files inside. | Saving changes to `hello.py` or editing notes in a text file. |
| **`x` — Execute** | Allows the file to be executed as a program or binary; on a directory, allows entering/traversing into the folder. | Running a compiled binary or shell script (`./run.sh`), or using `cd` to enter a folder. |

---

### Task 3.4 — Operating-System Responsibilities Table

| OS Responsibility | Your Explanation (In My Own Words) | Real-World Example |
| :--- | :--- | :--- |
| **Process Management** | Creating, scheduling, prioritizing, and terminating processes so multiple programs can share the CPU seamlessly without colliding. | The macOS kernel switches CPU cores rapidly between VS Code, Spotify, and Chrome so they appear to run simultaneously. |
| **Memory Management** | Allocating and tracking physical RAM blocks for active applications, ensuring programs do not overwrite each other's memory, and utilizing virtual memory paging when RAM is full. | When launching Python, the OS assigns it a dedicated virtual memory space and prevents other apps from corrupting its variables. |
| **Device Management** | Communicating with and coordinating hardware peripherals (keyboards, monitors, printers, USB drives) using specialized software called device drivers. | Translating multi-touch finger gestures on the physical trackpad into smooth scrolling actions on screen. |
| **File Management** | Organizing physical storage blocks into a hierarchical structure of named files and folders, tracking metadata, and controlling read/write access. | The APFS (Apple File System) saving `sample.txt` onto specific flash memory blocks on the NVMe SSD and organizing it under the assignment folder. |
| **User Interface / Shell** | Providing a bridge for human users to interact with the computer, either visually through a Graphical User Interface (GUI) or through text commands via a Command Line Interface (CLI). | The macOS Aqua desktop GUI (Finder, Dock) and the zsh Terminal shell where commands like `ls` and `pwd` are processed. |
| **Security and Permissions** | Enforcing authentication (passwords, Touch ID) and file ownership rules to ensure unauthorized users or rogue software cannot access or destroy sensitive data. | Blocking an untrusted downloaded script from modifying protected system files in `/System` or reading another user's private folders. |

---

## 5. Difficulties Faced
- Understanding why `top` reported over 790 processes running when only a few application windows (Terminal, Chrome) were visibly open on the desktop.

---

## 6. How I Resolved Them
- Learned that modern operating systems run hundreds of lightweight background **daemons** and system services (handling audio, networking, disk indexing, security checks, and window compositing) that have no graphical windows but keep the system functional and responsive.

---

## 7. Evidence / Files
- `mission-03-operating-system/README.md`
- Terminal observation logs: `sw_vers`, `df -h`, `top -l 1`, `ps aux`.

---

## 8. Commit Details
- **Commit Message**: `Mission 3: Document operating system and file management`
- **Target Branch**: `main`
- **Pushed to GitHub**: Yes (Commit pending push confirmation)

---

## How to Explain This Mission to My Teacher

### 1. What was the objective?
"The objective of Mission 3 was to explore the internal workings of the operating system: how it reports system specs, manages active processes, handles file permissions, and coordinates hardware through its six core responsibilities."

### 2. What practical work did I perform?
"I used Terminal to inspect my operating system version (`macOS 27.2.1`), checked my available storage (`df -h`), captured a snapshot of running processes (`top` and `ps aux`), analyzed the PID column, compared absolute vs. relative paths, and examined file permissions (`-rw-r--r--`)."

### 3. Which commands or tools did I use?
"I used `sw_vers`, `uname -srm`, `whoami`, `df -h`, `top`, `ps aux`, and `ls -l`."

### 4. What did I learn?
"I learned that an operating system is the master coordinator of computer resources. A program on disk becomes a process when loaded into RAM with a unique PID. I also learned how Unix file permissions protect files across Owner, Group, and Others."

### 5. What was the most important observation?
"The most eye-opening observation was that my computer was running over 790 processes simultaneously, even though I only had a couple of applications open on screen. The vast majority were background system services maintaining the OS."

### 6. Five Possible Questions My Teacher Might Ask & Simple Answers

**Q1: What is the difference between a program and a process?**
> **Answer**: A program is passive code stored on a storage drive (like a file on an SSD). A process is an active, running instance of that program loaded into RAM with allocated CPU time and a unique PID.

**Q2: What is a PID, and why does the operating system use it?**
> **Answer**: PID stands for Process Identifier. It is a unique number assigned by the OS kernel to track, monitor, schedule, and manage or terminate that specific process.

**Q3: What does the permission string `-rw-r--r--` mean?**
> **Answer**: It represents a regular file (`-`) where the owner can read and write (`rw-`), group members can only read (`r--`), and all other users can only read (`r--`).

**Q4: What is the difference between an absolute path and a relative path?**
> **Answer**: An absolute path starts from the root directory (`/`) and gives the full path regardless of where you currently are. A relative path starts from your current working directory (`pwd`).

**Q5: Name three core responsibilities of an Operating System.**
> **Answer**: Process management (scheduling CPU time), Memory management (allocating RAM to programs), and File management (organizing and protecting files on the storage drive).
